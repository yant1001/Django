from django.contrib.auth.models import AbstractUser
from django.db import models

# models.py 변경 시 마이그레이션 필수 (makemigrations -> migrate)
class User(AbstractUser):
    profile_image = models.ImageField(
        "프로필 이미지", upload_to="users/profile", blank=True
    )
    short_description = models.TextField("소개글", blank=True)