from django.conf.urls import url, include

from .views import (
    home,
    contact,
    gallery,
    about,
    )

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^contact/$', contact, name="contact"),
    url(r'^about/$', about, name="about"),
    url(r'^gallery/$', gallery, name="gallery"),
]