from rest_framework import serializers
from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    transcription = serializers.URLField(read_only=True)
    class Meta:
        model = Video
        fields = ('id', 'video', 'transcription')