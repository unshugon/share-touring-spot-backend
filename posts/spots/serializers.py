from typing_extensions import Required
from rest_framework import serializers
from .models import Post
from accounts.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "image",
            "content",
            "location",
            "created_at",
            "created_by",
            "is_deleted",
        )
