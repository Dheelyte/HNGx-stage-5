# # Install required libraries if not already installed
# # pip install SpeechRecognition pydub

# import speech_recognition as sr
# from pydub import AudioSegment
# from pydub.silence import split_on_silence
# from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip

# # Step 1: Transcribe audio from video
# video_path = 'test1.mp4'
# audio_path = 'test1.wav'
# recognizer = sr.Recognizer()

# def transcribe_audio(video_path):
#     audioclip = AudioFileClip(video_path)
#     audioclip.write_audiofile(audio_path)
#     with sr.AudioFile(audio_path) as source:
#         audio_data = recognizer.record(source)
#     transcription = recognizer.recognize_google(audio_data)  # You can choose a different recognizer

#     return transcription

# transcription = transcribe_audio(video_path)


# # Step 2: Split audio into segments based on silence
# audio = AudioSegment.from_file(audio_path)  # Convert audio to a compatible format
# min_silence_length = 1000  # Adjust this threshold as needed
# silence_threshold = -36  # Adjust this threshold as needed
# audio_segments = split_on_silence(audio, min_silence_len=min_silence_length, silence_thresh=silence_threshold)

# # Step 3: Generate subtitles with timestamps
# subtitles = []
# start_time = 0

# for segment in audio_segments:
#     end_time = start_time + len(segment) / 1000  # Convert milliseconds to seconds
#     sub_text = recognizer.recognize_google(segment)
#     subtitles.append((start_time, end_time, sub_text))
#     start_time = end_time


# # Step 4: Overlay subtitles on the video
# video = VideoFileClip(video_path)
# duration = video.duration

# subtitle_clips = []

# for start, end, sub_text in subtitles:
#     sub_clip = TextClip(sub_text, fontsize=36, color='white')  # Adjust fontsize and color
#     sub_clip = sub_clip.set_position(('center', 'bottom')).set_duration(end - start)
#     subtitle_clips.append(sub_clip)

# video_with_subtitles = CompositeVideoClip([video] + subtitle_clips)
# video_with_subtitles.write_videofile('output_with_subtitles.mp4')


# print(subtitle_clips)
# print(transcription)



# # # Install required libraries if not already installed
# # # pip install SpeechRecognition pydub

# # import speech_recognition as sr
# # from pydub import AudioSegment
# # from pydub.silence import split_on_silence
# # from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip

# # # Step 1: Transcribe audio from video
# # video_path = 'test1.mp4'
# # audio_path = 'test1.wav'
# # recognizer = sr.Recognizer()

# # def transcribe_audio(video_path):
# #     audioclip = AudioFileClip(video_path)
# #     audioclip.write_audiofile(audio_path)
# #     with sr.AudioFile(audio_path) as source:
# #         audio_data = recognizer.record(source)
# #     transcription = recognizer.recognize_google(audio_data) # You can choose a different recogni    
# #     return transcription

# # transcription = transcribe_audio(video_path)


# # # Step 2: Split audio into segments based on silence
# # audio = AudioSegment.from_file(audio_path) # Convert audio to a compatible format
# # min_silence_length = 1000 # Adjust this threshold as needed
# # silence_threshold = -36 # Adjust this threshold as needed
# # audio_segments = split_on_silence(audio, min_silence_len=min_silence_length, silence_thresh=silence_threshold)

# # # Step 3: Generate subtitles with timestamps
# # subtitles = []
# # start_time = 0

# # for segment in audio_segments:
# #     end_time = start_time + len(segment) / 1000 # Convert milliseconds to seconds
# #     sub_text = recognizer.recognize_google(segment)
# #     subtitles.append((start_time, end_time, sub_text))
# #     start_time = end_time


# # # Step 4: Overlay subtitles on the video
# # video = VideoFileClip(video_path)
# # duration = video.duration

# # subtitle_clips = []

# # for start, end, sub_text in subtitles:
# #     sub_clip = TextClip(sub_text, fontsize=36, color='white') # Adjust fontsize and color
# #     sub_clip = sub_clip.set_position(('center', 'bottom')).set_duration(end - start)
# #     subtitle_clips.append(sub_clip)

# # video_with_subtitles = CompositeVideoClip([video] + subtitle_clips)

# # # Set the duration of the output video
# # video_with_subtitles.set_duration(duration)

# # # Save the video with subtitles
# # video_with_subtitles.write_videofile('output_with_subtitles.mp4', codec='libx264')


# print(transcription)




# Install required libraries if not already installed
# pip install SpeechRecognition pydub

import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip
from moviepy.video.tools.subtitles import SubtitlesClip

# Step 1: Transcribe audio from video
video_path = 'test1.mp4'
audio_path = 'test1.wav'
recognizer = sr.Recognizer()

def transcribe_audio(video_path):
    audioclip = AudioFileClip(video_path)
    audioclip.write_audiofile(audio_path)
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
    transcription = recognizer.recognize_google(audio_data)  # You can choose a different recognizer

    return transcription

transcription = transcribe_audio(video_path)


# Step 2: Split audio into segments based on silence
audio = AudioSegment.from_file(audio_path)  # Convert audio to a compatible format
min_silence_length = 1000  # Adjust this threshold as needed
silence_threshold = -36  # Adjust this threshold as needed
audio_segments = split_on_silence(audio, min_silence_len=min_silence_length, silence_thresh=silence_threshold)

# Step 3: Generate subtitles with timestamps
subtitles = []
start_time = 0

for segment in audio_segments:
    end_time = start_time + len(segment) / 1000  # Convert milliseconds to seconds
    sub_text = recognizer.recognize_google(segment)
    subtitles.append((start_time, end_time, sub_text))
    start_time = end_time

# ... (previous code remains the same)

# Adjust min_silence_length and silence_threshold as needed

# Step 2: Split audio into fixed-duration segments
# audio = AudioSegment.from_file(audio_path)  # Convert audio to a compatible format
# segment_duration = 10 * 1000  # Set the duration of each segment in milliseconds (e.g., 10 seconds)

# # Calculate the number of segments
# num_segments = len(audio) // segment_duration

# # Print the duration of the audio to verify it loaded correctly
# print(f"Audio duration: {len(audio) / 1000} seconds")

# # Split the audio into segments of the specified duration
# audio_segments = [audio[i * segment_duration:(i + 1) * segment_duration] for i in range(num_segments)]

# # Print the number of segments found
# print(f"Number of segments: {len(audio_segments)}")

# Step 3: Generate subtitles with timestamps
subtitles = []
start_time = 0

for segment in audio_segments:
    end_time = start_time + len(segment) / 1000  # Convert milliseconds to seconds
    sub_text = recognizer.recognize_google(segment)
    subtitles.append((start_time, end_time, sub_text))
    start_time = end_time

# ... (rest of the code remains the same)



# Step 4: Overlay subtitles on the video
video = VideoFileClip(video_path)
duration = video.duration

subtitle_clips = []

for start, end, sub_text in subtitles:
    sub_clip = TextClip(sub_text, fontsize=36, color='white')  # Adjust fontsize and color
    sub_clip = sub_clip.set_position(('center', 'bottom')).set_duration(end - start)
    subtitle_clips.append(sub_clip)

video_with_subtitles = CompositeVideoClip([video] + subtitle_clips)  # Remove set_duration

# Save the video with subtitles
video_with_subtitles.write_videofile('output_with_subtitles.mp4', codec='libx264')


print(transcription)