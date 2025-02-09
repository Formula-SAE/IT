from Bot.Modules.Source.SubMenu import SubMenu
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes


class AdminMenu(SubMenu):

    def __init__(self):
        super().__init__()

        self.INTRO_MESSAGES = {

            "main_admin": "GESTIONE ADMIN",
        }

        self.KEYBOARDS = {

            "main_admin": InlineKeyboardMarkup(
                [[InlineKeyboardButton("Manda messaggio in un gruppo", callback_data='send_message')],
                 [InlineKeyboardButton("Aggiungi Admin 🟢", callback_data='add_admin')],
                 [InlineKeyboardButton("Rimuovi Admin 🔴", callback_data='remove_admin')],
                 [InlineKeyboardButton("🔙 Ritorna al menu principale", callback_data='back_main_menu')]]),

        }

    async def start_conversation(self, update: Update, context: ContextTypes.DEFAULT_TYPE, query=None,
                                 current_batch: str = None):
        self.query = query
        self.current_batch = current_batch
        await query.edit_message_text(self.INTRO_MESSAGES[current_batch], reply_markup=self.KEYBOARDS[current_batch])



