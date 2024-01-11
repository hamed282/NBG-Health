from django.contrib import admin
from .models import GalleryImageSlideModel, GalleryVideoSlideModel, GalleryContentModel


admin.site.register(GalleryImageSlideModel)
admin.site.register(GalleryVideoSlideModel)
admin.site.register(GalleryContentModel)

