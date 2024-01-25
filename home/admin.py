from django.contrib import admin
from .models import HomeHeaderModel, HomeFooterModel, HomeContentModel, TeamContentModel, TeamValuesContentModel,\
    TeamCategoryModel, TeamValuesModel, MoreLandingModel, TeamCategoryMemberModel, PaperCategoryModel, PaperDateModel,\
    PaperPdfModel


class PaperDateAdmin(admin.ModelAdmin):
    list_display = ['date']


class PaperCategoryAdmin(admin.ModelAdmin):
    list_display = ['category']


class PaperPdfAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(HomeHeaderModel)
admin.site.register(HomeFooterModel)
admin.site.register(HomeContentModel)
admin.site.register(TeamContentModel)
admin.site.register(TeamValuesContentModel)
admin.site.register(TeamCategoryModel)
admin.site.register(TeamCategoryMemberModel)
admin.site.register(TeamValuesModel)
admin.site.register(MoreLandingModel)
admin.site.register(PaperDateModel, PaperDateAdmin)
admin.site.register(PaperCategoryModel, PaperCategoryAdmin)
admin.site.register(PaperPdfModel, PaperPdfAdmin)




