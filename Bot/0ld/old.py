from pandas import read_csv, DataFrame, concat
from telegram import Update
from telegram.ext import Application, CommandHandler, filters
from make_video_from_name import and_his_name_is
from gifted import display_home_video
import re
import subprocess


current_video_process = None

async def start(update, context):
   await update.message.reply_text("Ciao! Sono Martino Campanaro e suono le campane")


async def help(update, context):
    await update.message.reply_text("""
    Sono disponibili i seguenti comandi:
    /start --> Messaggio di benvenuto 
    /help --> Questo messaggio
    /info --> Informazioni su bot
    """)


async def info(update, context):
    await update.message.reply_text("""
    Ciao, sono il Bot ufficiale della scuderia Apex Corse. Mi occupo di far entrare chi vuole entrare.
    """, parse_mode='Markdown')


@staticmethod
def convert_string(input_string):
    # Define a dictionary to map digits to letters
    char_mappings = {'8': 'B', '0': 'O', '1': 'I', '3': 'E', '5': 'S', "6": "G", "7": "T"}
    # Use regular expression to find characters and replace them with corresponding letters
    output_string = re.sub(r'\d', lambda x: char_mappings.get(x.group(0), x.group(0)), input_string)
    return output_string

# async def suona(update, context):
#     """Prendo il messaggio di chi scrive e mando in play il video"""
#     username = update.message.from_user.username
#     and_his_name_is(convert_string(username))


async def screensaver(update, context):
    global current_video_process
    if current_video_process:
        current_video_process.terminate()  # Terminate the current video process if it exists
    current_video_process = subprocess.Popen(["ffplay", "-loop", "0", "screensaver.gif"])  # Start playing the video


async def suona(update, context):
    global current_video_process
    if current_video_process:
        current_video_process.terminate()  # Terminate the current video process if it exists
    current_video_process = subprocess.Popen(["ffplay", "-loop", "2","custom_new.mp4"])  # Start playing the home video
    current_video_process.wait()
    current_video_process.terminate()
    await screensaver(update, context)



def main():

    # display_home_video("screensaver.mp4")
    # Telegram Bot token
    TOKEN = '6874444274:AAEpmunW4ddXyYtjaS7rSdZGUb4oLfKMU5A'
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("screensaver", screensaver))
    application.add_handler(CommandHandler("suona", suona))
    # application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_messages))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)



if __name__ == "__main__":
    main()