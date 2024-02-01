from rest_framework import serializers
from .models import HomeHeaderModel, HomeFooterModel, HomeContentModel, TeamContentModel,\
    MoreLandingModel, TeamValuesModel, TeamCategoryModel, TeamCategoryMemberModel, PaperCategoryModel, PaperPdfModel,\
    PaperDateModel, ConnectedModel


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


class TeamCategoryMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamCategoryMemberModel
        fields = ['title', 'name', 'image']


class TeamCategorySerializer(serializers.ModelSerializer):
    # category = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    team_category = TeamCategoryMemberSerializer(many=True, read_only=True)

    class Meta:
        model = TeamCategoryModel
        fields = ['header', 'team_category']


class PaperPdfSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaperPdfModel
        fields = ['title', 'pdf_file']


class PaperCategorySerializer(serializers.ModelSerializer):
    paper_category = PaperPdfSerializer(many=True, read_only=True)

    class Meta:
        model = PaperCategoryModel
        fields = ['category', 'paper_category']


class PaperDateSerializer(serializers.ModelSerializer):
    date_paper = PaperCategorySerializer(many=True, read_only=True)

    class Meta:
        model = PaperDateModel
        fields = ['date', 'date_paper']


class ConnectedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectedModel
        fields = ['first_name', 'last_name', 'hospital', 'specialty', 'email']


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectedModel
        fields = ['email']
