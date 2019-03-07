from django.shortcuts import render
from .forms import superheroApplicationForm

# Create your views here.

def index(request):
    form=superheroApplicationForm(request.POST)
    context={
        "form":form
    }
    return render(request,"superheroApp/index.html",context)

def submit(request):
    return render(request,"superheroApp/thanks.html")