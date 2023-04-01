from django.urls import path

from . import views
from .views import *

create_list = lambda name : {'post': name}


comment_list = views.CommentView.as_view({
    'get': 'list',
    'post': 'create',

})
comment_change = views.CommentView.as_view({
    'get': 'edit',
    'put': 'edit',
    'delete': 'edit',
})

urlpatterns = [
    path('login/', LoginViewSet.as_view(create_list('login')), name="login"),
    path('register/', RegisterViewSet.as_view(create_list('signup')), name='signup'),
    path("logout/", LogoutView.as_view(create_list('logout_api')), name="logout_api"),
    path('author/', AuthorView.as_view({'get': 'list'})),
    path('author/<int:pk>/', AuthorView.as_view({'get': 'retrieve'})),
    path('auth/comment/',comment_list, name='comments'),
    path('auth/comment/<int:pk>/',comment_change, name='comments'),
]