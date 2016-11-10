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

from ballerine_app.models import StaticText, HomeImage, MiniGallery, Gallery


def home(request):
    # static text
    home_title = get_object_or_404(StaticText, title="home_title")
    first_section_h1 = get_object_or_404(StaticText, title="first_section_main")
    first_section_p = get_object_or_404(StaticText, title="first_section_sub")
    second_section_p = get_object_or_404(StaticText, title="second_section_content")
    second_section_h2 = get_object_or_404(StaticText, title="second_section_title")
    third_section_p = get_object_or_404(StaticText, title="third_section_content")
    third_section_h2 = get_object_or_404(StaticText, title="third_section_title")
    social_2_link = get_object_or_404(StaticText, title="social_2_link")
    social_1_link = get_object_or_404(StaticText, title="social_1_link")
    social_2_text = get_object_or_404(StaticText, title="social_2_text")
    social_1_text = get_object_or_404(StaticText, title="social_1_text")
    footer_copy = get_object_or_404(StaticText, title="footer_copyright")

    # images
    first_section_bg = get_object_or_404(HomeImage, title="first_section_background")
    second_section_image = get_object_or_404(HomeImage, title="second_section_image")
    third_section_image = get_object_or_404(HomeImage, title="third_section_image")

    queryset_list = MiniGallery.objects.all().order_by("-id")
    print(queryset_list[0].image.url)

    context = {
        "title": "Antropova Anastasia",
        "first_section_h1": first_section_h1,
        "first_section_p": first_section_p,
        "second_section_p": second_section_p,
        "second_section_h2": second_section_h2,
        "social_2_link": social_2_link,
        "social_1_link": social_1_link,
        "social_2_text": social_2_text,
        "social_1_text": social_1_text,
        "footer_copy": footer_copy,
        "third_section_p": third_section_p,
        "third_section_h2": third_section_h2,
        "first_section_bg": first_section_bg,
        "second_section_image": second_section_image,
        "third_section_image": third_section_image,
        "mini_gallery": queryset_list,
    }

    return render(request, "home.html", context)

def contact(request):
    context = []
    return render(request, "home.html", context)

def gallery(request):
    images = Gallery.objects.all().order_by("-id")

    gallery_title = get_object_or_404(StaticText, title="gallery_title")
    footer_copy = get_object_or_404(StaticText, title="footer_copyright")

    fotorama_background = get_object_or_404(HomeImage, title="fotorama_background")

    context = {
        "images": images,
        "footer_copy": footer_copy,
        "gallery_title": gallery_title,
        "fotorama_background": fotorama_background,
    }
    return render(request, "gallery.html", context)

def about(request):
    context = []
    return render(request, "about.html", context)