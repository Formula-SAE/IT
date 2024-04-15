from gtts import gTTS
from moviepy.editor import AudioFileClip, ColorClip, VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip
from pydub import AudioSegment


def text_to_speech(text, filename='output.mp3', duration=0.9, target_fps=30.070):
    # Initialize gTTS (Google Text-to-Speech) with the given text
    tts = gTTS(text=text, lang='it')

    # Save the audio file with the given filename
    tts.save(filename)

    # Load the saved audio file
    audio_clip = AudioSegment.from_file(filename)

    # Get the duration of the audio clip
    current_duration = len(audio_clip) / 1000  # Duration in seconds

    # If the duration is shorter, concatenate silence
    if current_duration < duration:
        silence_duration = int((duration - current_duration) * 1000)  # Duration in milliseconds
        silence = AudioSegment.silent(duration=silence_duration)
        audio_clip += silence
    # If the duration is longer, trim the audio
    elif current_duration > duration:
        audio_clip = audio_clip[:int(duration * 1000)]  # Trim audio

    # Set the target frame rate for the audio clip
    audio_clip.set_frame_rate(int(target_fps))

    # Set the target channels for the audio clip (stereo)
    audio_clip.set_channels(2)

    # Export the adjusted audio clip to the same filename
    audio_clip.export(filename, format='mp3')



def create_static_image_with_text_video(text_audio_file, duration, output_file, text,
                                        text_position=None, text_color='white', fontsize=200):
    # Load the audio file
    audio_clip = AudioFileClip(text_audio_file)

    # Create a blank image clip with the same duration as the audio clip
    blank_image_clip = ColorClip(size=(1920, 1080), color=(0, 0, 0), duration=duration)  # Adjust size as needed

    # Add text to the image clip
    text_clip = TextClip(text, fontsize=fontsize, color=text_color, align='center')
    text_clip = text_clip.set_duration(duration)

    # If text_position is not specified, calculate center position
    if text_position is None:
        text_width, text_height = text_clip.size
        text_x = (1920 - text_width) / 2
        text_y = (1080 - text_height) / 2
        text_position = (text_x, text_y)

    # Set the position of the text clip
    text_clip = text_clip.set_position(text_position)

    # Ensure text is fully visible
    while text_clip.size[1] > 1080 or text_clip.size[0] > 1920:
        fontsize -= 10
        text_clip = TextClip(text, fontsize=fontsize, color=text_color, align='center')
        text_clip = text_clip.set_duration(duration)
        text_clip = text_clip.set_position(text_position)

    # Combine the blank image clip and the text clip
    final_clip = CompositeVideoClip([blank_image_clip, text_clip])

    # Set the audio to the final clip
    final_clip = final_clip.set_audio(audio_clip)

    # Write the final clip to a video file
    final_clip.write_videofile(output_file, fps=24, codec="libx264")


def and_his_name_is(name_and_floor):
    # Generate audio file for the text "Peppe Blunda" with a duration of 0.9 seconds
    text_to_speech(name_and_floor, "output.mp3", duration=2.5)

    # Create a static image video clip with the generated audio
    create_static_image_with_text_video("output.mp3", 1.5, "generated_text_video.mp4", name_and_floor)

    # Combine the static image video with the "custom_jhon.mp4" video
    video_file = "customino.mp4"
    generated_text_clip = VideoFileClip("generated_text_video.mp4")  # Load video file using VideoFileClip
    output_file = "final_video.mp4"
    insertion_time = 1.2  # The time in seconds where you want to insert the text into the video

    # Load the "custom_jhon.mp4" video
    custom_jhon_clip = VideoFileClip(video_file)

    # Insert the generated text clip into the "custom_jhon.mp4" video
    final_clip = concatenate_videoclips([custom_jhon_clip.subclip(0, insertion_time),
                                         generated_text_clip,
                                         custom_jhon_clip.subclip(insertion_time)])

    # Write the final video to a file
    final_clip.write_videofile(output_file, codec="libx264", fps=24)