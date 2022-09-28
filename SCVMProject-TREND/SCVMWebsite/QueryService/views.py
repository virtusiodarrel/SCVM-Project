from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import messages
from .forms import BDSAForm
from .forms import UploadFileForm
from .models import BDSA
import json
from django.core.paginator import Paginator
from django.forms.models import model_to_dict

# Create your views here.
def home(request):
    last_five = BDSA.objects.all().order_by('?')[:5]
    return render(request, 'QueryService/home.html', {'cve': last_five})


def search_cve(request):
    if request.method == "POST":
        searched = request.POST['searched']
        cves = BDSA.objects.filter(cve_id__contains=searched)
        return render(request, 'QueryService/show_cve.html', {'searched':searched, 'cves':cves})
    else:
        return render(request, 'QueryService/search_cve.html', {})

def list_cve(request):
    cve_list = BDSA.objects.all() #.order_by('-cve_id')
    # Pagination
    page = Paginator(cve_list.order_by('-cve_id'), 10) # show 10 per page
    pages = request.GET.get('page')
    cves = page.get_page(pages)
    nums = "a" * cves.paginator.num_pages
    return render(request, 'QueryService/list_cve.html', {'cve_list': cve_list, 'cves': cves, 'nums':nums})

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
            show_json(i, duplicate, added)
        if len(duplicate)>0:
            return render(request, 'QueryService/show_json.html', {'msg': "File duplicates", 'duplicate': duplicate})
        elif len(file)>1:
            return render(request, 'QueryService/show_json.html', {'msg': "Files added to the database", 'duplicates': added})
        else: 
            return render(request, 'QueryService/show_json.html', {'msg': "File added to the database", 'duplicate': added})
    else:
        form = UploadFileForm
    return render(request, 'QueryService/upload_json.html', {'form': form})

def show_json(file, duplicate, added):
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

