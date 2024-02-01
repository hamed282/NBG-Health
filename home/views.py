from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HomeHeaderModel, HomeFooterModel, HomeContentModel, TeamContentModel,\
    MoreLandingModel, TeamValuesModel, TeamCategoryModel, PaperDateModel, PaperPdfModel, PaperCategoryModel,\
    ConnectedModel, EmailModel
from .serializers import HomeHeaderSerializer, HomeFooterSerializer, HomeContentSerializer,\
    TeamContentSerializer, TeamValuesSerializer, MoreLandingSerializer, TeamCategorySerializer,\
    PaperDateSerializer, PaperPdfSerializer, PaperCategorySerializer, ConnectedSerializer, EmailSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


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


class MoreLandingView(APIView):
    def get(self, request):
        more_landing = MoreLandingModel.objects.all()
        ser_more_landing = MoreLandingSerializer(instance=more_landing, many=True)

        return Response(data={'more_landing': ser_more_landing.data})


class PaperPdfView(APIView):
    def get(self, request):
        paper_pdf = PaperDateModel.objects.all()
        ser_paper_pdf = PaperDateSerializer(instance=paper_pdf, many=True)

        return Response(data=ser_paper_pdf.data)


# class PdfFilter(filter.FilterSet):
#     title = filter.CharFilter(field_name='date', lookup_expr='iexact')


class SearchPdfTitleView(viewsets.ModelViewSet):
    queryset = PaperPdfModel.objects.all()
    serializer_class = PaperPdfSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['date']
    # filterset_class = PdfFilter
    search_fields = ['title']
    # search_fields = ['date', 'date_paper__paper_category__title']
    ordering_fields = '__all__'


class SearchPdfCategoryView(viewsets.ModelViewSet):
    queryset = PaperCategoryModel.objects.all()
    serializer_class = PaperCategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['date']
    # filterset_class = PdfFilter
    search_fields = ['category']
    # search_fields = ['date', 'date_paper__paper_category__title']
    ordering_fields = '__all__'


class SearchPdfDateView(viewsets.ModelViewSet):
    queryset = PaperDateModel.objects.all()
    serializer_class = PaperDateSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['date']
    # filterset_class = PdfFilter
    search_fields = ['date']
    # search_fields = ['date', 'date_paper__paper_category__title']
    ordering_fields = '__all__'


class ConnectedView(APIView):
    def post(self, request):
        form = request.data
        ser_data = ConnectedSerializer(data=form)
        if ser_data.is_valid():
            ConnectedModel.objects.create(first_name=ser_data.validated_data['first_name'],
                                          last_name=ser_data.validated_data['last_name'],
                                          hospital=ser_data.validated_data['hospital'],
                                          specialty=ser_data.validated_data['specialty'],
                                          email=ser_data.validated_data['email'],)
        return Response(data='successfully')


class EmailView(APIView):
    def post(self, request):
        form = request.data
        ser_data = EmailSerializer(data=form)
        if ser_data.is_valid():
            EmailModel.objects.create(email=ser_data.validated_data['email'])

        return Response(data='Successfully')
