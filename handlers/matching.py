from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime, timedelta
import random

# Simpan timestamp pemakaian per user buat cooldown
user_cooldown = {}

async def matching(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    user_id = update.effective_user.id

    # Pastikan command hanya dipakai di grup
    if chat.type not in ["group", "supergroup"]:
        await update.message.reply_text(
            "❌ Command ini hanya bisa dipakai di grup." 
            if context.user_data.get("lang", "id") == "id"
            else "❌ This command can only be used in groups."
        )
        return

    now = datetime.utcnow() + timedelta(hours=7)  # Asia/Jakarta timezone
    lang = context.user_data.get("lang", "id")

    # Cek cooldown per user
    last_used = user_cooldown.get(user_id)
    if last_used and (now - last_used).total_seconds() < 3600:
        remaining = int(3600 - (now - last_used).total_seconds()) // 60
        msg = (
            f"⏳ Kamu baru bisa cari pasangan lagi dalam {remaining} menit."
            if lang == "id" else
            f"⏳ You can match again in {remaining} minutes."
        )
        await update.message.reply_text(msg)
        return

    user_cooldown[user_id] = now

    # Ambil anggota grup yang eligible (tidak ignore)
    admins = await chat.get_administrators()
    members = [admin.user for admin in admins]
    members.append(update.effective_user)

    eligible = [u for u in members if not context.user_data.get("ignore", False)]

    if len(eligible) < 2:
        msg = (
            "❌ Gagal mencarikan pasangan. Terlalu sedikit user yang bisa dijodohkan."
            if lang == "id" else
            "❌ Failed to match. Not enough eligible users!"
        )
        await update.message.reply_text(msg)
        return

    chosen = random.sample(eligible, 2)
    name1 = chosen[0].mention_html()
    name2 = chosen[1].mention_html()
    score = random.randint(0, 100)

    if lang == "id":
        text = (
            f"💘 <b>Pasangan Hari Ini ({now.strftime('%d %B %Y')})</b>\n\n"
            f"{name1} ❤️ {name2}\n"
            f"Semoga cinta kalian abadi 💞\n\n"
            f"📊 <b>Keserasian:</b> {score}%\n"
            f"🔁 Pasangan baru hanya bisa dipilih setelah 1 jam ⏰"
        )
    else:
        text = (
            f"💘 <b>Today's Couple ({now.strftime('%d %B %Y')})</b>\n\n"
            f"{name1} ❤️ {name2}\n"
            f"May your love last forever 💞\n\n"
            f"📊 <b>Compatibility:</b> {score}%\n"
            f"🔁 A new match can be chosen after 1 hour ⏰"
        )

    await update.message.reply_html(text)