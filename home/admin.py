from django.contrib import admin
from .models import HomeHeaderModel, HomeFooterModel, HomeContentModel, TeamContentModel, TeamValuesContentModel,\
    TeamPersonModel, TeamValuesModel, MoreLandingModel


admin.site.register(HomeHeaderModel)
admin.site.register(HomeFooterModel)
admin.site.register(HomeContentModel)
admin.site.register(TeamContentModel)
admin.site.register(TeamValuesContentModel)
admin.site.register(TeamPersonModel)
admin.site.register(TeamValuesModel)
admin.site.register(MoreLandingModel)
