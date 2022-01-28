from rest_framework import serializers
from .models import UserAccount


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = [
            "userId",
            "username",
            "email",
            "password",
        ]

    def create(self, validated_data):
        user = UserAccount.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"],
        )

        return user
