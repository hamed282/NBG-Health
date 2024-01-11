from rest_framework.views import APIView
from rest_framework.response import Response
from .models import GalleryImageSlideModel, GalleryVideoSlideModel, GalleryContentModel
from .serializers import GalleryImageSlideSerializer, GalleryContentSerializer, GalleryVideoSlideSerializer


class GalleryView(APIView):

    def get(self, request):
        image_slide = GalleryImageSlideModel.objects.all()
        ser_image_slide = GalleryImageSlideSerializer(instance=image_slide, many=True)

        video_slide = GalleryVideoSlideModel.objects.all()
        ser_video_slide = GalleryVideoSlideSerializer(instance=video_slide, many=True)

        content = GalleryContentModel.objects.all()
        ser_content = GalleryContentSerializer(instance=content, many=True)

        return Response(data={'image_slide': ser_image_slide.data, 'video_slide': ser_video_slide.data,
                              'content': ser_content.data})

