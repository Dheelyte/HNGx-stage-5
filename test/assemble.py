from moviepy.editor import AudioFileClip
import assemblyai as aai
import time

name = time.time()

aai.settings.api_key = "0c371e21a64a4fc5972bf00771f9af86"

video_path = f"test2.mp4"
audio_path = f"{name}.wav"

audioclip = AudioFileClip(video_path)
audioclip.write_audiofile(audio_path)

transcriber = aai.Transcriber()

transcript = transcriber.transcribe(audio_path)

subtitles_output = transcript.export_subtitles_vtt()

with open(f"{name}.vtt", 'x') as f:
    f.write(subtitles_output)
