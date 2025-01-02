from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes, ConversationHandler

from Bot.Modules.Source.Stop import stop
from Bot.Modules.Source.Start import Start
from Bot.Modules.Shared.Query import (InsertGroup, CheckUserExists, CheckGroupExists, CheckUserExistsInGroup,
                                      InsertUniqueUser, InsertUserInGroup)
from Bot.Modules.Source.Remote.RemoteSession import download_file
from Bot.Modules.Source.Utility import *


async def button_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Every time a button is pressed"""

    if update.callback_query.message.chat.type != "private":
        await group_conversation(update, context)
    else:
        await private_conversation(update, context)


async def group_conversation(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    match query.data:
        case "add_members":
            if not CheckUserExistsInGroup(-query.from_user.id, -query.message.chat.id):
                InsertUserInGroup(query.from_user.id, query.from_user.username, query.message.chat.title, False, True, False)
                if not CheckGroupExists(-query.message.chat.id):
                    InsertGroup(-query.message.chat.id, query.message.chat.title)
                if not CheckUserExists(-query.from_user.id):
                    InsertUniqueUser(-query.from_user.id, query.from_user.username, False, True, False)

                await context.bot.send_message(chat_id=query.from_user.id,
                                           text=f'Ciao {query.from_user.username}, '
                                                f'ti sei aggiunto con successo ai tag per il gruppo {query.message.chat.title}')


async def private_conversation(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    if "ConversationManager" not in context.user_data:
        message_id = query.message.message_id
        chat_id = query.message.chat_id
        await context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="Il Bot si è riavviato per aggiornarsi 😃.\nPremi /start e ricominciamooo!! 😊"
        )
        return

    if "first_start" in context.user_data:
        context.user_data['first_start'] = False

    # active_conversation = context.user_data["ConversationManager"].get_active_conversation()
    # current_batch = context.user_data["ConversationManager"].get_current_conversation_batch(context)
    # print("##################")
    # print(active_conversation, current_batch)
    # print("##################")

    match query.data:

        case 'back_main_menu':
            delete_all_conversations(context)
            await Start().start_conversation(update, context)

        case 'stop':
            delete_all_conversations_and_manager(context)
            await stop(update, context)

        # ----- ADMIN MENU -----

        case "main_admin":
            delete_all_conversations(context)
            # TODO

        case _:
            pass


async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Every time something is typed"""
    if update.message.chat.type == "private":
        active_conversation = context.user_data["ConversationManager"].get_active_conversation()
        current_batch = context.user_data["ConversationManager"].get_current_conversation_batch(context)

        # print("##################")
        # print(active_conversation, current_batch)
        # print("##################")

        conversation_id = safe_hash_name(active_conversation, current_batch)

        await context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)


def delete_all_conversations(context: ContextTypes.DEFAULT_TYPE):
    """Every time user goes to main menu, the conversation manager will be empty automatically"""
    context.user_data["ConversationManager"].set_active_conversation('')


def delete_all_conversations_and_manager(context: ContextTypes.DEFAULT_TYPE):
    """User for stop the Bot"""
    for _class in CONVERSATION_CLASSES:
        if _class in context.user_data:
            context.user_data.pop(_class)
