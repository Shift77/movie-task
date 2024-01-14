from rest_framework import serializers
from .models import Movie, Category, Rating


class CategorySerializer(serializers.ModelSerializer):
    '''Serializer for Category model.'''

    class Meta:
        model = Category
        fields = ['id' ,'name', 'parent']

    def create(self, validated_data):
        validated_data.pop('id', None)
        return super().create(validated_data)


class RatingSerializer(serializers.ModelSerializer):
    '''serializer for rating model.'''
    class Meta:
        model = Rating
        fields = ['id', 'movie', 'score']

    def create(self, validated_data):
        validated_data.pop('id', None)
        return super().create(validated_data)


class MovieSerializer(serializers.ModelSerializer):
    '''Serializer for movie model.'''
    # movie_ratings = RatingSerializer(many=True, read_only=True)
    average_score = serializers.ReadOnlyField(source='get_average_score')
    class Meta:
        model = Movie
        fields = ['id', 'name', 'category', 'image', 'average_score']

    def create(self, validated_data):
        validated_data.pop('id', None)
        return super().create(validated_data)
