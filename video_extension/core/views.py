from rest_framework.response import Response
from .serializers import VideoSerializer
from rest_framework.views import APIView
from rest_framework import status
from .models import Video

def transcribe(video_name):
    import os
    from moviepy.editor import AudioFileClip
    import assemblyai as aai
    import time

    name = time.time()

    aai.settings.api_key = "0c371e21a64a4fc5972bf00771f9af86"

    #video_path = f"test2.mp4"
    audio_path = os.path.join('media', 'audio', f"{name}.wav")
    video_path = os.path.join('media', 'videos', video_name)

    print("===============================", audio_path, video_name)

    audioclip = AudioFileClip(video_path)
    audioclip.write_audiofile(audio_path)

    transcriber = aai.Transcriber()

    transcript = transcriber.transcribe(audio_path)

    subtitles_output = transcript.export_subtitles_vtt()

    subtitle_path = os.path.join('media', 'transcriptions', f"{name}.vtt")

    with open(subtitle_path, 'x') as f:
        f.write(subtitles_output)
    
    subtitle_url = f"/media/transcriptions/{name}.vtt"
    return subtitle_url


class VideoHandler(APIView):

    def get(self, request):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            video_url = Video.objects.get(id=instance.id).video.url
            video_name = video_url.split('/')[-1]
            transcription = transcribe(video_name)
            serializer.save(transcription=transcription)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)