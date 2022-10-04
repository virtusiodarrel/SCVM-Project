from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import messages
import random
from .forms import BDSAForm
from .forms import UploadFileForm
from .models import BDSA
import json
from django.core.paginator import Paginator
from django.forms.models import model_to_dict

# Create your views here.
def home(request):
    last_five = list(BDSA.objects.all())
    if len(last_five) > 5:
        random_five = random.sample(last_five, 5)
        return render(request, 'QueryService/home.html', {'cve': random_five})
    else:
        return upload_json(request)


def search_cve(request):
    if request.method == 'GET':
        searched = request.GET.get('searched').upper()
        if searched:
            cve_search = BDSA.objects.filter(cve_id__icontains=searched)
            if len(cve_search)==1:
                cve = cve_search[0]
                return render(request, 'QueryService/show_cve.html', {'cve': cve})
            paginator = Paginator(cve_search.order_by('-cve_id'), 13)  # show 10 per page
            try:
                page = int(request.GET.get('page', '1'))
            except:
                page = 1
            try:
                cves = paginator.page(page)
            except:
                cves = paginator.page(1)
            index = cves.number - 1
            max_index = len(paginator.page_range)
            start_index = index - 2 if index >= 2 else 0
            end_index = index + 2 if index <= max_index - 2 else max_index
            page_range = list(paginator.page_range)[start_index:end_index]
            return render(request, 'QueryService/search_cve.html', {'searched':searched, 'cve_search':cve_search, 'cves': cves, 'page_range': page_range})
        else:
            return render(request, 'QueryService/search_cve.html', {})

def list_cve(request):
    cve_list = BDSA.objects.all()
    # Pagination
    paginator = Paginator(cve_list.order_by('-cve_id'), 10)  # show 10 per page
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        cves = paginator.page(page)
    except:
        cves = paginator.page(1)
    index = cves.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 2 if index >= 2 else 0
    end_index = index + 2 if index <= max_index - 2 else max_index
    page_range = list(paginator.page_range)[start_index:end_index]
    return render(request, 'QueryService/list_cve.html', {'cve_list': cve_list, 'cves': cves, 'page_range': page_range})

def show_cve(request, cve_id):
    cve = BDSA.objects.get(cve_id=cve_id)
    return render(request, 'QueryService/show_cve.html', {'cve': cve})

def upload_json(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES.getlist('file')
        duplicate = []
        added = []
        for i in file:
            read_json(i, duplicate, added)
        if len(duplicate)>0:
            return render(request, 'QueryService/read_json.html', {'msg': "File duplicates", 'duplicate': duplicate})
        elif len(file)>1:
            return render(request, 'QueryService/read_json.html', {'msg': "Files added to the database", 'duplicate': added})
        else: 
            return render(request, 'QueryService/read_json.html', {'msg': "File added to the database", 'duplicate': added})
    else:
        form = UploadFileForm
    return render(request, 'QueryService/upload_json.html', {'form': form})

def read_json(file, duplicate, added):
    cve_id = file.name.split('_')[0]
    details = file.read()
    bdsa_id = json.loads(details)['name']
    title = json.loads(details)['title']
    content = json.loads(details)
    content_formatted = json.dumps(content, indent=3)
    if (BDSA.objects.filter(cve_id=cve_id).exists() or BDSA.objects.filter(bdsa_id=bdsa_id).exists()):
        duplicate.append(cve_id)
    else:
        BDSA.objects.create(cve_id=cve_id, bdsa_id=bdsa_id, title=title, json_raw=content_formatted)
        added.append(cve_id)
    return 

