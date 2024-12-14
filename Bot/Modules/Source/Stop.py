from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """End conversation manually"""
    if "first_start" in context.user_data:
        context.user_data.pop("first_start")
        await update.callback_query.edit_message_text(text="👋🏽 Ciao, buona giornata! 👋🏽")
        context.user_data.pop("initial_message")
        return ConversationHandler.END


async def stop_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """End conversation by user command"""
    if "first_start" in context.user_data:
        context.user_data.pop("first_start")
        await context.bot.edit_message_text(chat_id=update.message.chat_id,
                                            message_id=context.user_data["initial_message"].message_id,
                                            text="👋🏽 Ciao, buona giornata! 👋🏽")
        context.user_data.pop("initial_message")
        return ConversationHandler.END
