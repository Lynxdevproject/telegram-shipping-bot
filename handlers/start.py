from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🇮🇩 Bahasa Indonesia", callback_data="lang_id")],
        [InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🌐 Pilih bahasa / Choose your language:",
        reply_markup=reply_markup
    )

async def set_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    bot_username = (await context.bot.get_me()).username

    if query.data == "lang_id":
        context.user_data["lang"] = "id"
        keyboard = [
            [InlineKeyboardButton("➕ Undang ke Grup", url=f"https://t.me/{bot_username}?startgroup=true")],
            [InlineKeyboardButton("👤 Developer", url="https://t.me/itsmelynxs")]
        ]
        await query.edit_message_text(
            "👋 *Ini Shipping Bot!*\n\n"
            "🔮 Bot lucu-lucuan buat jodoh-jodohan random di grup 💞\n"
            "🛠 Terinspirasi dari bot Discord *ahippering*\n\n"
            "📲 Klik tombol di bawah buat undang ke grup!",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )

    elif query.data == "lang_en":
        context.user_data["lang"] = "en"
        keyboard = [
            [InlineKeyboardButton("➕ Add Me to Group!", url=f"https://t.me/{bot_username}?startgroup=true")],
            [InlineKeyboardButton("👤 Developer", url="https://t.me/itsmelynxs")]
        ]
        await query.edit_message_text(
            "👋 *This Is Shipping Bot!*\n\n"
            "🔮 A joke bot to randomly ship people in your group 💞\n"
            "🛠 Inspired by *ahippering* bot from Discord\n\n"
            "📲 Click the button below to add me to your group!",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )