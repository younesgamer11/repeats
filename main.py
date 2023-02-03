# coding: utf8
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import TOKEN
import telegram

updater = Updater(token=TOKEN, use_context=True)

def echo(update, context):
	if update.message.text == '/start':
		context.bot.send_message(chat_id=update.effective_chat.id, text='Привет, я простой эхо бот, созданный ChatGPT, напиши мне что-нибудь и я пришлю тебе это в ответ.')
	else:
		context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher = updater.dispatcher
dispatcher.add_handler(echo_handler)
updater.start_polling()






# for admin
# @bot.message_handler(commands=['stat'])
# def send_welcome(message):
# 	if message.chat.id == ADMIN:
# 		stat = f'<b>📊 Статистика.</b>\n\n🔄 Количество пользователей: {countusers()}'
# 		bot.send_message(ADMIN, text=stat, parse_mode="html")