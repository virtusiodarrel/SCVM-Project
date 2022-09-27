from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import BDSAForm
from .forms import UploadFileForm
from .models import BDSA
import json
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, 'QueryService/home.html', {})

def add_cve(request):
    submitted = False
    if request.method == "POST":
        form = BDSAForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Added to Database!')
            return HttpResponseRedirect('/add_cve?submitted=True')
    else:
        form = BDSAForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'QueryService/add_cve.html', {'form':form, 'submitted':submitted})

def search_cve(request):
    if request.method == "POST":
        searched = request.POST['searched']
        cves = BDSA.objects.filter(cve_id__contains=searched)
        return render(request, 'QueryService/search_cve.html', {'searched':searched, 'cves':cves})
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
    cve = BDSA.objects.get(pk=cve_id)
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
    desc = json.loads(details)['description']
    tech_desc = json.loads(details)['technicalDescription']
    solution = json.loads(details)['solution']
    if (BDSA.objects.filter(cve_id=cve_id).exists() or BDSA.objects.filter(bdsa_id=bdsa_id).exists()):
        duplicate.append(cve_id)
    else:
        BDSA.objects.create(cve_id=cve_id, bdsa_id=bdsa_id, title=title, description=desc, technical_description=tech_desc, solution=solution)
        added.append(cve_id)
    return

