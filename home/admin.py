from django.contrib import admin
from .models import HomeHeaderModel, HomeFooterModel, HomeContentModel, TeamContentModel, TeamValuesContentModel,\
    TeamCategoryModel, TeamValuesModel, MoreLandingModel, TeamCategoryMemberModel, PaperCategoryModel, PaperDateModel,\
    PaperPdfModel


admin.site.register(HomeHeaderModel)
admin.site.register(HomeFooterModel)
admin.site.register(HomeContentModel)
admin.site.register(TeamContentModel)
admin.site.register(TeamValuesContentModel)
admin.site.register(TeamCategoryModel)
admin.site.register(TeamCategoryMemberModel)
admin.site.register(TeamValuesModel)
admin.site.register(MoreLandingModel)
admin.site.register(PaperCategoryModel)
admin.site.register(PaperDateModel)
admin.site.register(PaperPdfModel)
