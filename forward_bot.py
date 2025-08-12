from telegram.ext import Updater, MessageHandler, Filters

BOT_TOKEN = "8051531632:AAH38Z78kEEnNPJOtYouAytZg-xxqSmsf30"
DESTINATION_CHANNEL = "-1002386689030"  # Or channel ID like -100xxxxxxxxxx

def forward_message(update, context):
    context.bot.forward_message(
        chat_id=DESTINATION_CHANNEL,
        from_chat_id=update.message.chat_id,
        message_id=update.message.message_id
    )

updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.all & ~Filters.command, forward_message))

updater.start_polling()
updater.idle()
