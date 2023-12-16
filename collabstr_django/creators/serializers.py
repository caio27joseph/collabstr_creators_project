from rest_framework import serializers
from .models import Creator, Content


class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = ["name", "username", "rating", "platform"]

    def validate_rating(self, value):
        if not (0 <= value <= 5):
            raise serializers.ValidationError("Rating must be between 0 and 5.")
        return value


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ["creator", "url"]

    def validate_url(self, value):
        return value
