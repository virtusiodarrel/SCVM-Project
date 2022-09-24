from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import BDSAForm
from .forms import UploadFileForm
from .models import BDSA
import json

# Create your views here.
def home(request):
    return render(request, 'QueryService/home.html', {})

def add_cve(request):
    submitted = False
    if request.method == "POST":
        form = BDSAForm(request.POST)
        if form.is_valid():
            form.save()
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
    cve_list = BDSA.objects.all()
    return render(request, 'QueryService/list_cve.html', {'cve_list': cve_list})

def show_cve(request, cve_id):
    cve = BDSA.objects.get(pk=cve_id)
    return render(request, 'QueryService/show_cve.html', {'cve': cve})

def upload_json(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES.getlist('file')
        duplicate = []
        for i in file:
            read_json(i, duplicate)
        
        if len(duplicate)>0:
            return HttpResponse("Duplicates for "+ ', '.join(duplicate))
        if len(file)>1:
            return HttpResponse("Files added to database")
        else: 
            return HttpResponse("File added to database")
    else:
        form = UploadFileForm
    return render(request, 'QueryService/upload_json.html', {'form': form})

def read_json(file, duplicate):
    cve_id = file.name.split('_')[0]
    details = file.read()
    bdsa_id = json.loads(details)['name']
    if (BDSA.objects.filter(cve_id=cve_id).exists() or BDSA.objects.filter(bdsa_id=bdsa_id).exists()):
        duplicate.append(cve_id)
        return
    else:
        BDSA.objects.create(cve_id=cve_id, bdsa_id=bdsa_id)
    return 

