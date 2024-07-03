
"""

    IL TEAM IT BENE SUPREMO, IL TEAM IT - IL TEAM IT

"""

from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, filters, CallbackQueryHandler, CallbackContext
from make_video_from_name import and_his_name_is
from gifted import display_home_video
import re
from playsound import playsound
import subprocess
from os import path, getcwd
from random import choice
from datetime import time
from pandas import read_csv, concat, DataFrame
from time import sleep


current_video_process = None
# TODO: messaggi programmati in base agli utenti importanti


@staticmethod
def create_fronzoli():
    try:
        file_csv = open("users_to_tag.csv", "xt")
        file_csv.close()
        with open("users_to_tag.csv", "w") as f:
            f.write("user,id")
    except FileExistsError:
        pass

    try:
        file_txt = open("stato_Aula.txt", "xt")
        file_txt.close()
        with open("stato_Aula.txt", "w") as f:
            f.write(0)
    except FileExistsError:
        pass

    try:
        file_txt = open("chassis_users_to_tag.txt", "xt")
        file_txt.close()
        with open("stato_Aula.txt", "w") as f:
            f.write(0)
    except FileExistsError:
        pass


@staticmethod
def already_in(username_id: str, df_name: str) -> bool:
    """Verifica se l'utente che manda un messaggio è già registrato"""
    df_dict = {"spam": "users_to_tag.csv", "chassis": "chassis_users_to_tag.csv"}
    df = read_csv(df_dict[df_name], engine="c")
    if df[df["id"] == username_id].size > 0:
        return True
    else:
        return False


@staticmethod
def convert_string(input_string: str) -> str:
    # Define a dictionary to map digits to letters
    char_mappings = {'8': 'B', '0': 'O', '1': 'I', '3': 'E', '5': 'S', "6": "G", "7": "T"}
    # Use regular expression to find characters and replace them with corresponding letters
    output_string = re.sub(r'\d', lambda x: char_mappings.get(x.group(0), x.group(0)), input_string)
    output_string = output_string.replace("_", "").replace("-", "").replace("*", "")
    return output_string



@staticmethod
async def open_video() -> None:
    global current_video_process
    if current_video_process:
        current_video_process.terminate()  # Terminate the current video process if it exists
    current_video_process = subprocess.Popen(
        ["ffplay", "-loop", "1", "final_video.mp4"])  # Start playing the video


@staticmethod
async def close_video() -> None:
    global current_video_process
    sleep(10)
    if current_video_process:
        current_video_process.terminate()  # Terminate the current video process if it exists


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


async def stato_Aula(update, context):
    status_file = path.join(getcwd(), "stato_Aula.txt")
    if path.exists(status_file):
        with open(status_file, "r") as file:
            status = int(file.readline())
        if status == 1:
            messsaggi_preimpostati = [
                "sei fortunato l'Aula Falcon è aperta!",
                "sei stato baciato da Salvatore Papa!",
                "oggi sei fortunato",
                "venga non cincischi!",
                "per sta volta ti è andata bene",
                "spero tu abbia un giorno produttivo nell'Aula!",
                "ancora perdi tempo?",
                "arricampati!",
                "vieni a darmi un bacino"
            ]
            messaggio_preimpostato = choice(messsaggi_preimpostati)
            await update.message.reply_text(f"Ehy {update.message.from_user.username}, {messaggio_preimpostato}")
        else:
            messsaggi_preimpostati = [
                "oggi ti è andata male",
                "non hai speranze",
                "ti sembra il momento?",
                "ci sono solo io ma sono un bot e non posso aprirti",
                "uffa ancora non c'è nessuno",
                "solo non si vedono i capi repartooo, non c'è nessuno"
            ]
            messaggio_preimpostato = choice(messsaggi_preimpostati)
            await update.message.reply_text(f"Ehy {update.message.from_user.username}, {messaggio_preimpostato}")
    else:
        # Creo il file se non esiste già
        with open(status_file, "w") as file:
            file.write("")


async def apri_Aula(update, context):
    username = update.message.from_user.username
    status_file = path.join(getcwd(), "stato_Aula.txt")
    with open(status_file, "w") as file:
        file.write("1")
    messsaggi_preimpostati = [
        "hai aperto l'Aula Falcon ma non ti credere un esperto",
        "si ma calmati",
        "finalmente che Alosi aspettava te",
        "alla buon'ora",
        "uffa mi devo alzare",
        "in ritardo ma va bene",
        "ancora perdi tempo?",
        "era ora",
        "vieni che mi sento solo"
    ]
    messaggio_preimpostato = choice(messsaggi_preimpostati)
    await update.message.reply_text(f"Ok {username}, {messaggio_preimpostato}")


async def chiudi_Aula(update, context):
    username = update.message.from_user.username
    status_file = path.join(getcwd(), "stato_Aula.txt")
    with open(status_file, "w") as file:
        file.write("0")
    messsaggi_preimpostati = [
        "mi spiace ma è giusto così",
        "non lasciarmi solo per troppo tempo",
        "torna presto ho bisogno di te",
        "quando torni mi dai un bacino?",
        "finalmente ve ne andate",
        "ma dove andate? Posso venire pure io?",
        "buona serata",
        "batti panni libera tutti",
        "ma sappi che sto piangendo"
    ]
    messaggio_preimpostato = choice(messsaggi_preimpostati)
    await update.message.reply_text(f"Ok {username}, {messaggio_preimpostato}")


async def daily_chiudi_Aula(update, context):
    status_file = path.join(getcwd(), "stato_Aula.txt")
    with open(status_file, "w") as file:
        file.write("0")


async def spam_store_user_4tag(update, context):
    df = read_csv("users_to_tag.csv", engine="c")
    username = update.message.from_user.first_name
    username_id = int(update.message.from_user.id)
    if not already_in(username_id, "spam"):
        new_username = DataFrame({'user': username,
                                        'id': username_id}, index=[df.shape[0] + 1])
        df = concat([df, new_username])
        df.to_csv("users_to_tag.csv", index=False)
        await update.message.reply_text(f"Grazie {update.message.from_user.username}, ora sei nel giro")


async def store_chassis_user_4tag(update, context):
    df = read_csv("chassis_users_to_tag.csv", engine="c")
    username = update.message.from_user.first_name
    username_id = int(update.message.from_user.id)
    if not already_in(username_id, "chassis"):
        new_username = DataFrame({'user': username,
                                        'id': username_id}, index=[df.shape[0] + 1])
        df = concat([df, new_username])
        df.to_csv("chassis_users_to_tag.csv", index=False)
        await update.message.reply_text(f"Grazie {update.message.from_user.username}, ora sei nel giro")


async def tag_all_spam(update, context):
    df = read_csv("users_to_tag.csv", engine="c")
    tagged_users = []
    for index, row in df.iterrows():
        username = row["user"]
        id = int(row["id"])
        tagged_user = f'<a href="tg://user?id={id}">{username}</a>'
        tagged_users.append(tagged_user)
    tagged_users_str = '\n'.join(tagged_users)
    messsaggi_preimpostati = [
        "Il dovere chiama",
        "Fatevi sentire",
        "Oggi tocca a voi",
        "Ecco i Boss",
        "Siete sempre nel mio cuore",
        "Vi voglio bene"
    ]
    messaggio_preimpostato = choice(messsaggi_preimpostati)
    await update.message.reply_html(f"{messaggio_preimpostato}\n{tagged_users_str}")


async def tag_all_chassis(update, context):
    df = read_csv("chassis_users_to_tag.csv", engine="c")
    tagged_users = []
    for index, row in df.iterrows():
        username = row["user"]
        id = int(row["id"])
        tagged_user = f'<a href="tg://user?id={id}">{username}</a>'
        tagged_users.append(tagged_user)
    tagged_users_str = '\n'.join(tagged_users)
    messsaggi_preimpostati = [
        "Il dovere chiama",
        "Fatevi sentire",
        "Oggi tocca a voi",
        "Ecco i Boss",
        "Siete sempre nel mio cuore",
        "Vi voglio bene"
    ]
    messaggio_preimpostato = choice(messsaggi_preimpostati)
    await update.message.reply_html(f"{messaggio_preimpostato}\n{tagged_users_str}")


async def tag_all_admin(update, context):
    chat_id = update.message.chat_id
    tagged_users = []
    administrators = await context.bot.get_chat_administrators(chat_id)
    for admin in administrators[1:]:
        tagged_user = f'<a href="tg://user?id={admin.user.id}">{admin.user.first_name}</a>'
        tagged_users.append(tagged_user)
    tagged_users_str = '\n'.join(tagged_users)
    messsaggi_preimpostati = [
        "Il dovere chiama",
        "Fatevi sentire",
        "Oggi tocca a voi",
        "Ecco i Boss",
        "Siete sempre nel mio cuore",
        "Vi voglio bene"
    ]
    messaggio_preimpostato = choice(messsaggi_preimpostati)
    await update.message.reply_html(f"{messaggio_preimpostato}\n{tagged_users_str}")



async def screensaver(update, context):
    global current_video_process
    if current_video_process:
        current_video_process.terminate()  # Terminate the current video process if it exists
    current_video_process = subprocess.Popen(["ffplay", "-loop", "0", "screensaver.gif"])  # Start playing the video



async def suona(update, context):
    """Prendo il messaggio di chi scrive e mando in play l'audio"""
    username = update.message.from_user.username
    keyboard = [[InlineKeyboardButton("Piano Terra", callback_data=f'T:{username}')],
                [InlineKeyboardButton("Primo Piano", callback_data=f'1:{username}')],
                [InlineKeyboardButton("Secondo Piano", callback_data=f'2:{username}')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Scegli che operazione effettuare, altrimenti fai altro', reply_markup=reply_markup)


async def button_callback(update, context):
    query = update.callback_query
    azione = query.data.split(":")[0]
    username = query.data.split(":")[1]

    await query.edit_message_text("Ok, suono il campanello")

    match azione:
        case 'T':
            username_and_floor = username + "\nal piano terra"
            and_his_name_is(convert_string(username_and_floor))
            await open_video()
            await close_video()
            await query.edit_message_text("Campanello suonato")

        case '1':
            username_and_floor = username + "\nal primo piano"
            and_his_name_is(convert_string(username_and_floor))
            await open_video()
            await close_video()
            await query.edit_message_text("Campanello suonato")

        case '2':
            username_and_floor = username + "\nal secondo piano"
            and_his_name_is(convert_string(username_and_floor))
            await open_video()
            await close_video()
            await query.edit_message_text("Campanello suonato")


    
async def connect(fittizio):
	subprocess.run(['globalprotect', 'connect', '--portal', 'vpngp.unipa.it'])




def main():
    # Telegram Bot token
    with open("toke.txt", "r") as file:
        TOKEN = file.read()
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("help", help))
    # application.add_handler(CommandHandler("screensaver", screensaver))
    application.add_handler(CommandHandler("suona", suona))
    application.add_handler(CommandHandler("stato_Aula", stato_Aula))
    application.add_handler(CommandHandler("apri_Aula_Falcon", apri_Aula))
    application.add_handler(CommandHandler("chiudi_Aula_Falcon", chiudi_Aula))
    application.add_handler(CommandHandler("in_spam", spam_store_user_4tag))
    application.add_handler(CommandHandler("sono_di_chassis", store_chassis_user_4tag))
    application.add_handler(CommandHandler("all_spam", tag_all_spam))
    application.add_handler(CommandHandler("all_chassis", tag_all_chassis))
    # application.add_handler(CommandHandler("all_admin", tag_all_admin))
    application.add_handler(CallbackQueryHandler(button_callback))
    
    job_queue = application.job_queue
    # job_queue.run_repeating(connect, interval=1800, first=5)
    job_queue.run_daily(daily_chiudi_Aula, time=time(hour=4, minute=0, second=0))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)



if __name__ == "__main__":
    create_fronzoli()
    main()

