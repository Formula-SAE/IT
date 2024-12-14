
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from Bot.Modules.Shared.Query import GetStatoAula, SetStatoAula
from random import choice

async def stato_aula(update: Update, context: ContextTypes.DEFAULT_TYPE):
    status = GetStatoAula("AulaFalcon")
    if status:
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


async def apri_aula(update: Update, context: ContextTypes.DEFAULT_TYPE):
    SetStatoAula("AulaFalcon", True)
    username = update.message.from_user.username
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


async def chiudi_aula(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.from_user.username
    SetStatoAula("AulaFalcon", False)
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


async def daily_chiudi_aula(update: Update, context: ContextTypes.DEFAULT_TYPE):
    SetStatoAula("AulaFalcon", False)