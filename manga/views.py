import django_filters
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Manga, Genre
from .paginations import MangaPagination
from .serializers import MangaDetailSerializer, MangaListSerializer, GenreSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class MangaView(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        SearchFilter,
    ]
    search_fields = ["eng_name",'id', "rus_name", "type", "genre__name"]
    filterset_fields = ["type", "genre__name", "eng_name", "rus_name"]
    pagination_class = MangaPagination
    

    @action(detail=True, permission_classes = [IsAuthenticatedOrReadOnly])
    def edit(self,request, *args, **kwargs):
        manga = self.get_object()
        serializer = MangaDetailSerializer(manga)
        return Response(serializer.data)

class GenreView(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = []
    authentication_classes = []




