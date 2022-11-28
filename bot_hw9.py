from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5732407963:AAHLw5WMib1EfOOgABvYv_qTdExoJl7qEg8')
updater = Updater(token='5732407963:AAHLw5WMib1EfOOgABvYv_qTdExoJl7qEg8')
dispatcher = updater.dispatcher


def start(update, context):
    text = update.message.text.split()
    list = []
    for elem in text:
        if 'абв' not in elem:
            list.append(elem)
    context.bot.send_message(update.effective_chat.id, ' '.join(list))


start_handler = MessageHandler(Filters.text, start)
dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()