import logging
from Bot.Modules.Source.Utility import *
from Bot.Modules.Shared.Configs import LoadConfigs, get_token
from Bot.Modules.Source.Start import Start
from Bot.Modules.Source.Stop import stop_command
from Bot.Modules.Source.Suona.PlayCampanello import suona, personal
from Bot.Modules.Source.Tagging.TagMembers import add_members, tag_members
from Bot.Modules.Source.AulaManager.StatoAula import stato_aula, chiudi_aula, daily_chiudi_aula, apri_aula
from Bot.Modules.Source.ActionRouting import handle_messages, button_callbacks

from datetime import time

from telegram import Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    MessageHandler,
    filters
)

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def main() -> None:
    """Run the bot"""
    # Create the Application and pass the bot's token
    LoadConfigs()
    application = Application.builder().token(get_token()).build()

    application.add_handler(CommandHandler("start", Start().start_conversation))
    application.add_handler(CommandHandler("stop", stop_command))
    application.add_handler(CommandHandler("suona", suona))
    application.add_handler(CommandHandler("personal", personal))
    application.add_handler(CommandHandler("tag_members", tag_members))
    application.add_handler(CommandHandler("add_members", add_members))
    application.add_handler(CommandHandler("stato_aula", stato_aula))
    application.add_handler(CommandHandler("chiudi_aula", chiudi_aula))
    application.add_handler(CommandHandler("apri_aula", apri_aula))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_messages))
    application.add_handler(CallbackQueryHandler(button_callbacks))

    job_queue = application.job_queue
    job_queue.run_daily(daily_chiudi_aula, time=time(hour=4, minute=0, second=0))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
