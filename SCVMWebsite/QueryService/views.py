from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import BDSAForm
from .models import BDSA

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