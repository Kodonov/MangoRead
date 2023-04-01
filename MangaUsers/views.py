from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework import viewsets
from base.permission import  IsAuthor
from .models import User, Comment
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    LogoutSerializer,
     AuthorSerializer,
    MangaCommentListSerializer,
    CommentAddSerializer,
)

class RegisterViewSet(GenericViewSet):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(**serializer.validated_data)
        user.save()
        return Response(data=serializer.data, status=HTTP_201_CREATED)


class LoginViewSet(GenericViewSet):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid():
                username = request.data["username"]
                password = request.data["password"]
                user = authenticate(username=username, password=password)
                if user is None:
                    return Response("User not found,Please try again !")

                access = AccessToken.for_user(user)
                refresh = RefreshToken.for_user(user)
                response_data = {
                    "status": status.HTTP_200_OK,
                    "user": username,
                    "access": str(access),
                    "refresh": str(refresh),
                }
                return Response(data=response_data)

            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(
            data={"message": 'Not founde ERORR'})

class LogoutView(GenericViewSet):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data="Logouted", status=status.HTTP_204_NO_CONTENT)



class AuthorView(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = MangaCommentListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, permission_classes = [IsAuthor])
    def edit(self, request, *args, **kwargs):
        comment = self.get_object()
        serializer = CommentAddSerializer(comment)
        return Response(serializer.data)
