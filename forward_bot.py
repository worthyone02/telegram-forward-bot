from telegram.ext import Updater, MessageHandler, Filters

# === BOT CONFIG ===
TOKEN = "8051531632:AAHLkFNnjxyQzLV8EoycAMbhaG2j0rGsrr4"  # Example: "1234567890:ABCdefGhijKLMnopQRstUVwxyZ"
SOURCE_CHAT_ID = "-1002552543046"  # Example: "-1001234567890"
SOURCE_TOPIC_ID = "75"  # Example: "55"
DESTINATION_CHAT_ID = "-1002386689030"  # Example: "-1009876543210"

# === FORWARD FUNCTION ===
def forward_from_topic(update, context):
    message = update.message

    # Convert to int for comparison
    if (
        str(update.effective_chat.id) == SOURCE_CHAT_ID
        and str(message.message_thread_id) == SOURCE_TOPIC_ID
    ):
        # Forward based on type without exposing original sender
        if message.text:
            context.bot.send_message(chat_id=int(DESTINATION_CHAT_ID), text=message.text)
        elif message.photo:
            context.bot.send_photo(
                chat_id=int(DESTINATION_CHAT_ID),
                photo=message.photo[-1].file_id,
                caption=message.caption
            )
        elif message.audio:
            context.bot.send_audio(
                chat_id=int(DESTINATION_CHAT_ID),
                audio=message.audio.file_id,
                caption=message.caption
            )
        elif message.video:
            context.bot.send_video(
                chat_id=int(DESTINATION_CHAT_ID),
                video=message.video.file_id,
                caption=message.caption
            )
        else:
            # Fallback generic forward
            context.bot.forward_message(
                chat_id=int(DESTINATION_CHAT_ID),
                from_chat_id=int(SOURCE_CHAT_ID),
                message_id=message.message_id
            )

# === RUN BOT ===
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.all, forward_from_topic))

updater.start_polling()
print("Bot is running and filtering by topic...")
updater.idle()
