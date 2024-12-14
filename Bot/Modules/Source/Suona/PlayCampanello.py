import re
from playsound import playsound
from gtts import gTTS
from pydub import AudioSegment
from telegram import Update
from telegram.ext import ContextTypes
import os


def text_to_speech(text: str, filename: str, duration=0.9, target_fps=30.070):
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


def and_his_name_is_mp3(name: str):
    static_path = os.path.join(os.getcwd(), 'Modules', 'Source', "Suona")
    output_path = os.path.join(static_path, "output.mp3")
    jcena_path = os.path.join(static_path, "jcena.mp3")

    # Generate audio file for the text with the given name
    text_to_speech(name, output_path, duration=1.5)

    # Load the generated audio file
    generated_audio = AudioSegment.from_file(output_path)

    # Load the customino.mp3 file
    customino_audio = AudioSegment.from_file(jcena_path)

    # Split customino audio into two segments: before and after insertion point
    customino_before = customino_audio[:1200]
    customino_after = customino_audio[1200:]

    # Concatenate the segments with the generated audio in between
    final_audio = customino_before + generated_audio + customino_after

    # Export the final audio to a unique file
    final_path = os.path.join(static_path, f"final_audio.mp3")
    final_audio.export(final_path, format="mp3")

    return final_path


def convert_string(input_string: str) -> str:
    char_mappings = {'8': 'B', '0': 'O', '1': 'I', '3': 'E', '5': 'S', "6": "G", "7": "T"}
    output_string = re.sub(r'\d', lambda x: char_mappings.get(x.group(0), x.group(0)), input_string)
    output_string = output_string.replace("_", "").replace("-", "").replace("*", "")
    return output_string


async def suona(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Take user who have done the command and plays his name loudly"""
    username = update.message.from_user.first_name
    message = await update.message.reply_text("Ok, suono il campanello")
    audio_path = and_his_name_is_mp3(convert_string(username))
    audio_path = os.path.abspath(audio_path)
    playsound(audio_path)
    os.remove(audio_path)
    await message.edit_text("Campanello suonato, fatti trovare al primo piano")


async def personal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dispetto = str(update.message.text).replace("/personal ", "")
    static_path = os.path.join(os.getcwd(), 'Modules', 'Source', 'Suona')
    dispetto_path = os.path.join(static_path, 'dispetto.mp3')
    dispetto_path = os.path.abspath(dispetto_path)
    text_to_speech(dispetto, dispetto_path, duration=7)
    playsound(dispetto_path)
    os.remove(dispetto_path)
    await update.message.reply_text("Scherzetto compiuto :>")
