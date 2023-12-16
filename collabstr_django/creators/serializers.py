from rest_framework import serializers
from .models import Creator, Content


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ["url"]

    def validate_url(self, value):
        return value


class CreatorSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)  # Nested serializer for content

    class Meta:
        model = Creator
        fields = ["name", "username", "rating", "platform", "contents"]

    def validate_rating(self, value):
        if not (0 <= value <= 5):
            raise serializers.ValidationError("Rating must be between 0 and 5.")
        return value
