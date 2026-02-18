from rest_framework import serializers
from .models import User


# User serializers
class UserSerializer(serializers.ModelSerializer):

    # General purpose user serializer for profile views
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "full_name",
            "bio",
            "profile_picture",
            "reading_goal",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
        extra_kwargs = {
            "email": {"required": True},
            "reading_goal": {
                "min_value": 12,
                "max_value": 1000,
                "allow_null": True,
            },
        }

    def validate_reading_goal(self, value):
        if value and value < 12:
            raise serializers.ValidationError("Reading goal must be at least 12 books")
        return value


# Registration serializer
class UserRegistrationSerializer(serializers.ModelSerializer):

    # User registration with password confirmation

    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password_confirm"]

    def validate(self, data):
        if data["password"] != data["password_confirm"]:
            raise serializers.ValidationError("Passwords don't match")
        return data

    def create(self, validated_data):

        validated_data.pop("password_confirm")  # remove confirmation field
        user = User.objects.create_user(**validated_data)  # hashes password
        return user
