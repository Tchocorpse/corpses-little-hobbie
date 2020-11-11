from rest_framework import serializers
from .models import HelloTestMessage, MessageImageMap, ImageFileModel


class TestMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelloTestMessage
        fields = "__all__"


class ImageFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageFileModel
        fields = "__all__"


class MessageImageMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageImageMap
        fields = "__all__"
