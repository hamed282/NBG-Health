from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HomeHeaderModel, HomeFooterModel, HomeContentModel, TeamContentModel,\
    TeamValuesContentModel, MoreLandingModel, TeamValuesModel, TeamCategoryModel
from .serializers import HomeHeaderSerializer, HomeFooterSerializer, HomeContentSerializer,\
    TeamContentSerializer, TeamValuesSerializer, MoreLandingSerializer, TeamCategorySerializer


class HomeHeaderView(APIView):

    def get(self, request):
        home_header = HomeHeaderModel.objects.all()
        ser_home_header = HomeHeaderSerializer(instance=home_header, many=True)

        return Response(data={'home_header': ser_home_header.data})


class HomeFooterView(APIView):

    def get(self, request):
        home_footer = HomeFooterModel.objects.all()
        ser_home_footer = HomeFooterSerializer(instance=home_footer, many=True)

        return Response(data={'home_footer': ser_home_footer.data})


class HomeContentView(APIView):

    def get(self, request):
        home_content = HomeContentModel.objects.all()
        ser_home_content = HomeContentSerializer(instance=home_content, many=True)

        return Response(data={'home_content': ser_home_content.data})


class TeamContentView(APIView):

    def get(self, request):

        # serializer_class = TeamPersonSerializer
        team_content = TeamContentModel.objects.all()
        ser_team_content = TeamContentSerializer(instance=team_content, many=True)

        team_category = TeamCategoryModel.objects.all()
        ser_team_category = TeamCategorySerializer(instance=team_category, many=True)



        team_values = TeamValuesModel.objects.all()
        ser_team_values = TeamValuesSerializer(instance=team_values, many=True)
        # list_values = {}
        # print(ser_team_values.data)
        return Response(data={'team_content': ser_team_content.data, 'team_person': ser_team_category.data,
                              'our_values': ser_team_values.data})
        # return Response(data=ser_team_values.data)


class MoreLandingView(APIView):
    def get(self, request):
        more_landing = MoreLandingModel.objects.all()
        ser_more_landing = MoreLandingSerializer(instance=more_landing, many=True)

        return Response(data={'more_landing': ser_more_landing.data})
