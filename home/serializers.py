from rest_framework import serializers
from .models import HomeHeaderModel, HomeFooterModel, HomeContentModel, TeamContentModel,\
    TeamValuesContentModel, MoreLandingModel, TeamValuesModel, TeamCategoryModel, TeamCategoryMemberModel,\
    TeamCategoryModel


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


# class TeamPersonSerializer(serializers.ModelSerializer):
#     category = serializers.SlugRelatedField(read_only=True, slug_field='slug')
#
#     class Meta:
#         model = TeamPersonModel
#         fields = '__all__'
class TeamCategorySerializer(serializers.ModelSerializer):
    # category = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    header_category = serializers.StringRelatedField(many=True)

    class Meta:
        model = TeamCategoryModel
        fields = ['header', 'header_category']


class TeamCategoryMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamCategoryMemberModel
        fields = ['title', 'name', 'image']


class TeamContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeamContentModel
        fields = '__all__'


class TeamValuesSerializer(serializers.ModelSerializer):
    # team_values = serializers.SlugRelatedField(read_only=True, slug_field='values_description')
    list_values = serializers.StringRelatedField(many=True)

    class Meta:
        model = TeamValuesModel
        fields = ['values_title', 'list_values']


class MoreLandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoreLandingModel
        fields = '__all__'
