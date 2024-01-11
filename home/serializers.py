from rest_framework import serializers
from .models import HomeHeaderModel, HomeFooterModel, HomeContentModel, TeamPersonModel, TeamContentModel,\
    TeamValuesContentModel


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


class TeamPersonSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = TeamPersonModel
        fields = '__all__'


class TeamContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeamContentModel
        fields = '__all__'


class TeamValuesContentSerializer(serializers.ModelSerializer):
    values_title = serializers.SlugRelatedField(read_only=True, slug_field='values_title')

    class Meta:
        model = TeamValuesContentModel
        fields = '__all__'
