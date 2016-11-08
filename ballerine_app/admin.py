from django.contrib import admin
from ballerine_app.models import StaticText, HomeImage, MiniGallery, Gallery


# Register your models here.

class StaticTextModelAdmin(admin.ModelAdmin):
    list_display = ["title", "id"]
    list_display_links = ["title"]

    search_fields = ["title", "content"]

    class Meta:
        model = StaticText


class HomeImageModelAdmin(admin.ModelAdmin):
    list_display = ["title", "id"]
    list_display_links = ["title"]

    search_fields = ["title"]

    class Meta:
        model = HomeImage


class MiniGalleryModelAdmin(admin.ModelAdmin):
    list_display = ["title", "id"]
    list_display_links = ["title"]

    search_fields = ["title"]

    class Meta:
        model = MiniGallery


class GalleryModelAdmin(admin.ModelAdmin):
    list_display = ["title", "id"]
    list_display_links = ["title"]

    search_fields = ["title"]

    class Meta:
        model = Gallery

admin.site.register(StaticText, StaticTextModelAdmin)
admin.site.register(HomeImage, HomeImageModelAdmin)
admin.site.register(MiniGallery, MiniGalleryModelAdmin)
admin.site.register(Gallery, GalleryModelAdmin)