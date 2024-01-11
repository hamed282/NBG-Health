from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HomeHeaderModel, HomeFooterModel, HomeContentModel, TeamContentModel, TeamPersonModel,\
    TeamValuesContentModel, MoreLandingModel
from .serializers import HomeHeaderSerializer, HomeFooterSerializer, HomeContentSerializer, TeamPersonSerializer,\
    TeamContentSerializer, TeamValuesContentSerializer, MoreLandingSerializer


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
        team_content = TeamContentModel.objects.all()
        ser_team_content = TeamContentSerializer(instance=team_content, many=True)

        team_person = TeamPersonModel.objects.all()
        ser_team_person = TeamPersonSerializer(instance=team_person, many=True)

        team_values = TeamValuesContentModel.objects.all()
        ser_team_values = TeamValuesContentSerializer(instance=team_values, many=True)

        return Response(data={'team_content': ser_team_content.data, 'team_person': ser_team_person.data,
                              'team_values': ser_team_values.data})


class MoreLandingView(APIView):
    def get(self, request):
        more_landing = MoreLandingModel.objects.all()
        ser_more_landing = MoreLandingSerializer(instance=more_landing, many=True)

        return Response(data={'more_landing': ser_more_landing.data})
