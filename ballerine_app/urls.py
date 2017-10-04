from django.conf.urls import url, include
from django.conf.urls.static import static

from DancerPortfolio import settings
from .views import (
    home,
    contact,
    gallery,
    about,
    comment)

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^contact/$', contact, name="contact"),
    url(r'^about/$', about, name="about"),
    url(r'^gallery/$', gallery, name="gallery"),
    url(r'^comment/$', comment, name="comment"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)