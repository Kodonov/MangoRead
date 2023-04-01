from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken ,TokenError
from .models import User, Comment

class RegisterSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(min_length=8)
    username = serializers.CharField(min_length=4)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'nickname']
        extra_kwargs = {"password": {'write_only': True}}


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField()

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail("Invalid token")

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username', 'nickname', 'password')

class MangaCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text', 'manga', 'user']
        extra_kwargs = {"author": {"read_only": True}}

class AuthorSerializer(serializers.ModelSerializer):
    user_comments = MangaCommentListSerializer(many=True)
    class Meta:
        model = User
        fields = ('id','username', 'nickname', 'password', 'user_comments' )

class CommentAddSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    text = serializers.CharField(max_length=250)

    class Meta:
        model = Comment
        fields = ["text", "manga", 'user']

