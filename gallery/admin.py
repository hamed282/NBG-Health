from django.contrib import admin
from .models import GalleryImageSlideModel, GalleryVideoSlideModel, GalleryContentModel


class GalleryVideoSlideAdmin(admin.ModelAdmin):
    list_display = ['title']


class GalleryImageSlideAdmin(admin.ModelAdmin):
    list_display = ['title']


class GalleryContentAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(GalleryImageSlideModel, GalleryImageSlideAdmin)
admin.site.register(GalleryContentModel, GalleryContentAdmin)
admin.site.register(GalleryVideoSlideModel, GalleryVideoSlideAdmin)
