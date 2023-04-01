from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from MangaUsers.services.managers import CustomUser
from django.conf import settings
from manga.models import Manga

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, null=True, unique=True)
    nickname = models.EmailField(max_length=100,null=True )
    password = models.CharField(max_length=255)
    objects = CustomUser()
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

class Comment(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_comments"
    )
    text = models.TextField()

    def __str__(self):
        return f"{self.user} commented manga :{self.manga}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

