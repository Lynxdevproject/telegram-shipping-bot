from telegram import Update
from telegram.ext import ContextTypes

async def unignoreme(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "id")
    context.user_data["ignore"] = False

    if lang == "id":
        await update.message.reply_text(
            "✅ Kamu telah *diaktifkan kembali* untuk dijodohkan.\n"
            "💘 Siap-siap jadi korban cinta acak lagi!",
            parse_mode="Markdown"
        )
    else:
        await update.message.reply_text(
            "✅ You’ve been *reactivated* for matchmaking.\n"
            "💘 Get ready to be randomly shipped again!",
            parse_mode="Markdown"
        )