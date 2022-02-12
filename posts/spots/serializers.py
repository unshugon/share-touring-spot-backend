from rest_framework import serializers
from .models import Post
from accounts.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()
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

    def get_location(self, obj):
        if obj.location is not None:
            return {"lat": obj.location.x, "lng": obj.location.y}
