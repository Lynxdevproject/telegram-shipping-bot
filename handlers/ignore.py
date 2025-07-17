from telegram import Update
from telegram.ext import ContextTypes

async def ignoreme(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "id")
    context.user_data["ignore"] = True

    if lang == "id":
        await update.message.reply_text(
            "🚫 Kamu telah memilih untuk *tidak dijodohkan* oleh Shipping Bot.\n"
            "📵 Kamu akan dihindari dari pasangan di fitur /matching.\n\n"
            "💡 Gunakan /unignoreme kalau kamu berubah pikiran!",
            parse_mode="Markdown"
        )
    else:
        await update.message.reply_text(
            "🚫 You’ve chosen to *opt out* from being matched by Shipping Bot.\n"
            "📵 You will be excluded from pairing in the /matching feature.\n\n"
            "💡 Use /unignoreme if you change your mind!",
            parse_mode="Markdown"
        )