
from django.contrib.auth.base_user import BaseUserManager


class CustomUser(BaseUserManager):
    def _create_user(self, username, nickname,  password, **extra):
        user = self.model(username=username, nickname=nickname,  **extra)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def _create_admin(self, username, password, **extra):
        admin = self.model(username=username, password=password, **extra)
        admin.set_password(password)
        admin.save(using=self._db)
        return admin

    def create_user(self, username, nickname,  password):
        return self._create_user(username, nickname,  password)

    def create_superuser(self, username, password):
        return self._create_admin(username, password, is_superuser=True, is_staff=True)
