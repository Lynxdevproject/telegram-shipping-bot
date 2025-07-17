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

# Import handler modular
from handlers.start import start, set_language
from handlers.matching import matching
from handlers.ignore import ignoreme
from handlers.unignore import unignoreme
from handlers.identity_watcher import identity_watcher  # listener real-time deteksi perubahan identitas

# Load token dari .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # ⚙️ Command Handler
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("matching", matching))
    app.add_handler(CommandHandler("ignoreme", ignoreme))
    app.add_handler(CommandHandler("unignoreme", unignoreme))

    # 🌐 Callback handler untuk language selection
    app.add_handler(CallbackQueryHandler(set_language, pattern="^lang_"))

    # 🕵️‍♂️ Real-time identity watcher (always on listener)
    app.add_handler(MessageHandler(filters.ALL, identity_watcher))

    # 🚀 Run bot polling
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
