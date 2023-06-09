import openai
import telebot
import logging
import os
import time
import settings
settings.init()

openai.api_key = settings.api_key
bot = telebot.TeleBot(settings.telegram_token)

# Logging
if not os.path.exists('/tmp/bot_log/'):
    os.makedirs('/tmp/bot_log/')

logging.basicConfig(filename='/tmp/bot_log/log.txt', level=logging.ERROR)

def generate_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    return response["choices"][0]["text"]

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, 'Привет!\nЯ ChatGPT Telegram Bot\U0001F916\nЗадай мне любой вопрос и я постараюсь на него ответить')

@bot.message_handler(func = lambda message: message.text and (message.chat.type == "group" or message.chat.type == "supergroup") and message.text.startswith("/bot "))
def handle_command_group(message):
	prompt = message.text.replace("/bot ", "", 1)
	response = generate_response(prompt)
	bot.reply_to(message, text=response)

@bot.message_handler(func = lambda message: message.text and message.chat.type == "private")
def handle_message_private(message):
	prompt = message.text
	response = generate_response(prompt)
	bot.send_message(chat_id=message.from_user.id, text=response)

while True:
    try:
        bot.polling()
    except (telebot.apihelper.ApiException, ConnectionError) as e:
        logging.error(str(e))
        time.sleep(5)
        continue