from django.contrib import admin
from .models import HomeHeaderModel, HomeFooterModel, HomeContentModel


admin.site.register(HomeHeaderModel)
admin.site.register(HomeFooterModel)
admin.site.register(HomeContentModel)
