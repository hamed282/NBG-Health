from rest_framework import serializers
from .models import GalleryContentModel, GalleryVideoSlideModel, GalleryImageSlideModel


class GalleryImageSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImageSlideModel
        fields = '__all__'


class GalleryVideoSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryVideoSlideModel
        fields = '__all__'


class GalleryContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryContentModel
        fields = '__all__'
