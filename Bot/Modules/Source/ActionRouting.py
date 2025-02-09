from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes, ConversationHandler

from Bot.Modules.Source.Stop import stop
from Bot.Modules.Source.Start import Start
from Bot.Modules.Shared.Query import (InsertGroup, CheckUserExists, CheckGroupExists, CheckUserExistsInGroup,
                                      InsertUser, InsertUserInGroup, GetGroups, GetGroupName)
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
            add_user_in_group_tag(query)
            await context.bot.send_message(chat_id=query.from_user.id,
                                           text=f'Ciao {query.from_user.username}, '
                                                f'ti sei aggiunto con successo ai tag per '
                                                f'il gruppo {query.message.chat.title}')


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
            await context.user_data["Admin"].start_conversation(update=None, context=context, query=query,

                                                                current_batch="main_admin")
        # ----- SEND MESSAGE -----

        case "send_message":
            context.user_data["ConversationManager"].set_active_conversation("SendMessage")
            await context.user_data["SendMessage"].start_conversation(update=None, context=context, query=query,
                                                                      current_batch="send_message")

        case selected_group if selected_group in {str(id_group[1]) for id_group in GetGroups()}:
            context.user_data["SendMessage"].set_group_id(selected_group)
            keyboard = InlineKeyboardMarkup(
                [[InlineKeyboardButton("✔ Conferma", callback_data='acquire_message')],
                 [InlineKeyboardButton("🔙 Torna indietro", callback_data='main_admin')]])
            await query.edit_message_text(f"Hai scelto {GetGroupName(selected_group)}, confermi?", reply_markup=keyboard)

        case "acquire_message":
            await context.user_data["SendMessage"].forward_conversation(query, context,
                                                                        current_batch="acquire_message")

        case "message_done":
            await context.user_data["SendMessage"].end_conversation(update=update, context=context, query=query)

        # TODO:
        # add_admin, remove_admin

        # case _:
        #     pass


async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Every time something is typed"""
    if update.message.chat.type == "private":
        active_conversation = context.user_data["ConversationManager"].get_active_conversation()
        current_batch = context.user_data["ConversationManager"].get_current_conversation_batch(context)

        # print("##################")
        # print(active_conversation, current_batch)
        # print("##################")

        conversation_id = safe_hash_name(active_conversation, current_batch)

        if conversation_id == ACQUIRE_MESSAGE_TO_SEND:
            message_to_sent = update.message.text
            chat_id = update.message.chat_id
            message_id = update.message.message_id
            entities = update.message.entities
            await context.user_data["SendMessage"].acquire_conversation_param(context,
                                                                              previous_batch="acquire_group",
                                                                              current_batch="confirm_message",
                                                                              next_batch="message_done",
                                                                              chat_id=chat_id,
                                                                              message_id=message_id,
                                                                              typed_string=message_to_sent,
                                                                              entities=entities)

        await context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)


def add_user_in_group_tag(query):
    """Add user in Group"""

    if not CheckGroupExists(query.message.chat.id):
        InsertGroup(id_group=query.message.chat.id, group_name=query.message.chat.title)

    if not CheckUserExists(query.from_user.id):
        InsertUser(id_user=query.from_user.id, username=query.from_user.username,
                   isAdmin=False, isVerified=True, isHide=False)

    if not CheckUserExistsInGroup(id_user=query.from_user.id, id_group=query.message.chat.id):
        InsertUserInGroup(id_user=query.from_user.id, id_group=query.message.chat.id)


def delete_all_conversations(context: ContextTypes.DEFAULT_TYPE):
    """Every time user goes to main menu, the conversation manager will be empty automatically"""
    context.user_data["ConversationManager"].set_active_conversation('')


def delete_all_conversations_and_manager(context: ContextTypes.DEFAULT_TYPE):
    """User for stop the Bot"""
    for _class in CONVERSATION_CLASSES:
        if _class in context.user_data:
            context.user_data.pop(_class)
