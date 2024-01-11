from rest_framework.views import APIView
from rest_framework.response import Response
from .models import NewsModel
from .serializers import NewsSerializer


class NewsView(APIView):

    def get(self, request):
        news = NewsModel.objects.all()
        ser_news = NewsSerializer(instance=news, many=True)

        return Response(data={'news': ser_news.data})

