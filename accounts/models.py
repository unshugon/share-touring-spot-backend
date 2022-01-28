from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from uuid import uuid4


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            return ValueError("User must have an email")

        email = self.normalize_email(email).lower()
        user = self.model(username=username, email=email)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(email, username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    userId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField("メールアドレス", max_length=255, unique=True)
    username = models.CharField("名前", max_length=255, unique=True)
    created_at = models.DateTimeField("アカウント作成日", auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.email
