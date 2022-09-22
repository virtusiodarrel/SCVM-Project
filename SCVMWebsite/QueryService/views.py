from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import BDSAForm

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
        return render(request, 'QueryService/search_cve.html', {'searched':searched})
    else:
        return render(request, 'QueryService/search_cve.html', {})