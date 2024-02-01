from django.contrib import admin
from .models import HomeHeaderModel, HomeFooterModel, HomeContentModel, TeamContentModel, TeamValuesContentModel,\
    TeamCategoryModel, TeamValuesModel, MoreLandingModel, TeamCategoryMemberModel, PaperCategoryModel, PaperDateModel,\
    PaperPdfModel, ConnectedModel


class PaperDateAdmin(admin.ModelAdmin):
    list_display = ['date']


class PaperCategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'date']


class PaperPdfAdmin(admin.ModelAdmin):
    list_display = ['title']


class TeamCategoryAdmin(admin.ModelAdmin):
    list_display = ['header', 'priority']


class ConnectedAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'hospital', 'specialty', 'email']


admin.site.register(HomeHeaderModel)
admin.site.register(HomeFooterModel)
admin.site.register(HomeContentModel)
admin.site.register(TeamContentModel)
admin.site.register(TeamValuesContentModel)
admin.site.register(TeamCategoryModel, TeamCategoryAdmin)
admin.site.register(TeamCategoryMemberModel)
admin.site.register(TeamValuesModel)
admin.site.register(MoreLandingModel)
admin.site.register(PaperDateModel, PaperDateAdmin)
admin.site.register(PaperCategoryModel, PaperCategoryAdmin)
admin.site.register(PaperPdfModel, PaperPdfAdmin)
admin.site.register(ConnectedModel, ConnectedAdmin)
