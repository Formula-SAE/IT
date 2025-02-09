
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes, CallbackContext
from Bot.Modules.Source.SubMenu import SubMenu
from Bot.Modules.Source.Utility import *
from Bot.Modules.Source.Admin.AdminMenu import AdminMenu
from Bot.Modules.Source.Admin.SendMessage import SendMessage

from Bot.Modules.Source.ConversationManager import ConversationManager
from Bot.Modules.Shared.Query import GetIsAdmin


class Start(SubMenu):

    def __init__(self):
        super().__init__()

    async def start_conversation(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:

        if update.message.chat.type != "private":
            text = ("🏎 Ciao sono Martino 🏎\n"
                    "🦅 Bot ufficiale di Apex Corse 🦅\n\n"
                    "Posso:\n"
                    "-> Suonare il campanello dell'Aula Falcon /suona\n"
                    "-> Dirti se l'Aula è aperta o chiusa /stato\n"
                    "-> Puoi mettermi nel gruppo del tuo reparto e usarmi per taggare tutti /tag_members")
            await update.message.reply_text(text=text)
        else:

            text = "🏎 Ciao sono Martino 🏎\n\n"

            if GetIsAdmin(update.message.from_user.id):
                main_menu_keyboard = []
                classes_to_generate = {"ConversationManager": ConversationManager()}
                classes_to_generate |= {"Admin": AdminMenu(), "SendMessage": SendMessage()}

                # ----- BUTTONS -----

                admin = InlineKeyboardButton(text="👨🏽‍🔧 ADMIN MENU 🏽‍🔧", callback_data="main_admin")
                stop = InlineKeyboardButton(text="🛑 STOP 🛑", callback_data="stop")

                # -------------------

                # Eventualmente proteggere il DB da eventuali SQL Injection
                # che darebbe accesso a tutte le funzioni di Admin
                username = update.message.from_user.username
                text += f"👋🏽 {username}, è un piacere rivederti! 👋🏽\nCome posso aiutarti ? 👀"

                main_menu_keyboard.append([admin])
                main_menu_keyboard.append([stop])

                keyboard = InlineKeyboardMarkup(main_menu_keyboard)

                # Check if it is first start or not
                if "first_start" not in context.user_data:
                    initial_message = await update.message.reply_text(text=text, reply_markup=keyboard)
                    context.user_data['first_start'] = True
                    context.user_data['initial_message'] = initial_message
                    for key, value in classes_to_generate.items():
                        context.user_data[key] = value
                else:
                    await update.callback_query.edit_message_text(text=text, reply_markup=keyboard)

            else:
                text += (f'👋🏽 {update.message.from_user.username}, è un piacere! 👋🏽\n'
                         f'Mi spiace ma non sei abilitato a questa funzione 😁')
                await update.message.reply_text(text=text)
