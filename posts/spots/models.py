from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField("タイトル", max_length=50)
    image = models.ImageField(upload_to="images", verbose_name="イメージ画像")
    content = models.TextField("本文", max_length=500)
    created_at = models.DateTimeField("作成日", auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="作成者",
        blank=True,
        null=True,
    )
    is_deleted = models.BooleanField("削除判定", default=False)

    def __str__(self):
        return str(self.id) + " - " + self.title
