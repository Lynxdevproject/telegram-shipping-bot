import asyncio
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters
)
from dotenv import load_dotenv
import os

# 🔥 Anti-sleep setup buat Replit
from keep_alive import keep_alive
keep_alive()

# 📦 Import handlers modular
from handlers.start import start, set_language
from handlers.matching import matching
from handlers.ignore import ignoreme
from handlers.unignore import unignoreme
from handlers.identity_watcher import identity_watcher  # live detector perubahan nama

# 🌱 Load token dari .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # ✅ Command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("matching", matching))
    app.add_handler(CommandHandler("ignoreme", ignoreme))
    app.add_handler(CommandHandler("unignoreme", unignoreme))

    # 🌐 Callback untuk language choice
    app.add_handler(CallbackQueryHandler(set_language, pattern="^lang_"))

    # 🕵️ Real-time identity watcher (always on)
    app.add_handler(MessageHandler(filters.ALL, identity_watcher))

    # 🔁 Polling start
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
