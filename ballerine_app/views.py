from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages

from urllib.parse import quote_plus


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_protect







def home(request):

    context = {
        "title": "Antropova Anastasia",
    }

    return render(request, "home.html", context)

def contact(request):
    context = []
    return render(request, "home.html", context)

def gallery(request):
    context = []
    return render(request, "home.html", context)