from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import ToDoList,Item
from .models import Thinh
from .forms import Create_New_List

# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response,"main/base.html",{})




def home(response):
    return render(response,"main/home.html",{})

def thinh(response):
	return render(response,"main/base.html",{})

def create(response):
    if response.method == "POST":
        form = Create_New_List(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)   

    else:
         form = Create_New_List()
    return render(response, "main/create.html", {'form': form})



