from django.contrib import admin
from .models import NewsModel


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}


admin.site.register(NewsModel, NewsAdmin)

