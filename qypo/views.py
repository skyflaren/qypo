"""qypo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.http import HttpResponse, FileResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm

# def index(request):
#     return render(request,"index.html",{})

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            arr = request.POST.get("inputted_text").split("\n")

            ret = "{"

            for i in range(len(arr)):
                ret = ret + "\"" + arr[i][0:len(arr[i])-1] + "\"";
                if(i != len(arr)-1):
                    ret = ret + ", ";
            ret = ret + "}";

            return render(request, "done.html", context={"return": ret});

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'index.html', {'form': form})

def done(request):
    return render(request,"done.html", {})
