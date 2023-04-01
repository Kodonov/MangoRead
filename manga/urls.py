from django.urls import path
from . import views
from .views import *




manga_list = views.MangaView.as_view({
    'get': 'list',

})
manga_detail = views.MangaView.as_view({
    'get': 'retrieve',
})
manga_edit = views.MangaView.as_view({
    'get': 'edit',
    'post': 'edit',
    'put': 'edit',
    'patch': 'edit',
    'delete': 'edit'
})
genre_list = GenreView.as_view({
    'get': 'list',
})


urlpatterns = [
    path('manga/', manga_list, name='manga-list'),
    path('manga/<int:pk>/', manga_detail, name='manga-detail'),
    path('manga/<int:pk>/edit/', manga_edit, name='manga-edit'),
    path('genre/',genre_list, name='genres')

]
