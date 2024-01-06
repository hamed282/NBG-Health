from rest_framework import serializers
from .models import HomeHeaderModel, HomeFooterModel, HomeContentModel


class HomeHeaderSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = HomeHeaderModel
        fields = '__all__'


class HomeFooterSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = HomeFooterModel
        fields = '__all__'


class HomeContentSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = HomeContentModel
        fields = '__all__'
