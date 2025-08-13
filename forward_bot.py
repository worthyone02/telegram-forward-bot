import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.environ.get("8051531632:AAHLkFNnjxyQzLV8EoycAMbhaG2j0rGsrr4")
SOURCE_CHAT_ID = int(os.environ.get("-1002552543046"))       # group id
DESTINATION_CHAT_ID = int(os.environ.get("-1002386689030")) # channel id
SOURCE_TOPIC_ID = int(os.environ.get("75"))     # topic/thread id

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.effective_message

    # Only forward messages from the specific group + topic
    if msg.chat_id == SOURCE_CHAT_ID and msg.message_thread_id == SOURCE_TOPIC_ID:
        # Use copy_message to hide original sender
        await context.bot.copy_message(
            chat_id=DESTINATION_CHAT_ID,
            from_chat_id=msg.chat_id,
            message_id=msg.message_id
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward_message))

APP_URL = os.environ.get("APP_URL")
WEBHOOK_PATH = f"/{BOT_TOKEN}"

app.run_webhook(
    listen="0.0.0.0",
    port=int(os.environ.get("PORT", 8080)),
    url_path=BOT_TOKEN,
    webhook_url=f"{APP_URL}/{BOT_TOKEN}"
)
