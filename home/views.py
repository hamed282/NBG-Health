from rest_framework.views import APIView
from rest_framework.response import Response
# from course.models import CourseCategoryModel, CourseSubCategoryModel, CourseModel, SampleExerciseModel
# from blog.models import BlogModel
from .models import HomeHeaderModel, HomeFooterModel, HomeContentModel
# from course.serializers import CourseCategorySerializer, CourseSubCategorySerializer, CourseSerializer,\
#     SampleExerciseSerializer
from .serializers import HomeHeaderSerializer, HomeFooterSerializer, HomeContentSerializer
# from blog.serializers import BlogSerializer


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
