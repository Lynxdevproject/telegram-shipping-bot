async def identity_watcher(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    uid = user.id
    lang = context.user_data.get("lang", "id")

    # Data user sekarang
    current_name = user.full_name
    current_username = user.username or "—"

    # Ambil data sebelumnya
    prev_data = context.user_data.get("identity", {})
    prev_name = prev_data.get("name")
    prev_username = prev_data.get("username")

    # Simpan terbaru
    context.user_data["identity"] = {"name": current_name, "username": current_username}

    # Bandingkan
    if prev_name and (prev_name != current_name or prev_username != current_username):
        if lang == "id":
            msg = (
                "🕵️‍♂️ <b>Perubahan Terdeteksi!</b>\n"
                "💭 Selalu ada cara untuk menghindari perjodohan...\n\n"
                f"🔧 Nama Sebelumnya: <code>{prev_name}</code>\n"
                f"🔧 Username Sebelumnya: <code>@{prev_username}</code>"
            )
        else:
            msg = (
                "🕵️‍♂️ <b>Identity Change Detected!</b>\n"
                "💭 There's always a way to avoid matchmaking...\n\n"
                f"🔧 Previous Name: <code>{prev_name}</code>\n"
                f"🔧 Previous Username: <code>@{prev_username}</code>"
            )
        await update.message.reply_html(msg)