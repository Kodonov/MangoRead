from rest_framework import serializers
from manga.models import Manga, Genre



class MangaListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Manga
        fields = ("id", "eng_name", "rus_name", "poster", "avg_rating", "chapters_quantity", "genre", "likes")



class MangaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = ("id", "eng_name", "rus_name",
                  "poster", "avg_rating", "issue_year",
                  "type", "description", "likes", "created_at", "updated_at")


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ("id", "name")












