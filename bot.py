from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

BOT_TOKEN = "8548318351:AAFh_RzQZJUcwEzGeWXFezjjszK4w-s6NHc"
CHANNEL_ID = -1003282039080

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me a file.")

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    file = msg.document or msg.video or msg.audio
    if not file:
        return

    sent = await context.bot.send_document(
        chat_id=CHANNEL_ID,
        document=file.file_id
    )

    link = f"https://t.me/c/{str(CHANNEL_ID)[4:]}/{sent.message_id}"
    await msg.reply_text(f"File link:\n{link}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL, handle_file))
app.run_polling()
