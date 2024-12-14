from telegram import Update
from telegram.ext import ContextTypes
import os


def download_file(update: Update, context: ContextTypes.DEFAULT_TYPE, file_id: str, file_name: str):
    try:
        file = context.message.bot.get_file(file_id)
        download_path = os.path.join(os.getcwd(), file_name)

        file.download(download_path)
        print(f"File {file_name} downloaded successfully to {download_path}")
    except Exception as e:
        print(f"An error occurred while downloading the file: {e}")
