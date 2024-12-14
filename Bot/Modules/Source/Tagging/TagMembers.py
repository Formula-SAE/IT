
from Bot.Modules.Shared.Query import GetGroupUsers
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from random import choice

async def add_members(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("➕ Aggiungimi", callback_data='add_members')]])
    await update.message.reply_text("Ragazzi per favore cliccate il bottone, così vi aggiungo per il tag 😚",
                                    reply_markup=keyboard)


async def tag_members(update: Update, context: ContextTypes.DEFAULT_TYPE):

    tagged_users = [
        f'<a href="tg://user?id={users.id_telegram}">{users.username}</a>'
        for users in GetGroupUsers(update.message.chat.id)
    ]

    # Join tagged users into a single string
    tagged_users_str = '\n'.join(tagged_users)

    messsaggi_preimpostati = [
        "Il dovere chiama",
        "Fatevi sentire",
        "Oggi tocca a voi",
        "Ecco i Boss",
        "Siete sempre nel mio cuore",
        "Vi voglio bene"
    ]

    # Select a random message
    messaggio_preimpostato = choice(messsaggi_preimpostati)

    # Reply with the final message
    await update.message.reply_html(f"{messaggio_preimpostato}\n{tagged_users_str}")