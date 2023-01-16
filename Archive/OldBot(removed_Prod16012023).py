import telebot
import random
from telebot import types
import requests
from bs4 import BeautifulSoup as b

bot = telebot.TeleBot('telegram_token')

#Метод кнопка - отправка сообщения
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('➰Гороскоп')
    item2 = types.KeyboardButton('🌟Мотивация')
    item3 = types.KeyboardButton('🟧Новое')
    item4 = types.KeyboardButton('🎱Помогу принять решение')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup) 

first = ["Дорогая,", "Милая,", "Родная моя,", "Подруга,", "Драгоценная,", "Девочка моя,", "Подружка,", "Прекрасная моя,", "Свет очей моих,"]
second = ["сейчас  у меня болит голова😰", "а карандаш был красный, или я опять не угадала?🙃", "Лучше этого не делать", "Просто сделай это!😎", "Однозначно НЕТ📛", "Конечно же нет", "Да, да и ещё раз ДА!😍", "Сегодня лучше выпить винишка🍷", "ещё разок подумай над вопросом", "42😱", "в этой жизни нужно попровать всё, кроме этого конечно", "Попробуй спросить ещё раз", "завтра, всё завтра...", "забудь пожалуйста об этом", "если это из-за него, то лучше перестань об этом думать", "давай не сейчас. Я слишком занята😵", "напишу как узнаю🙄","ты самая крутая, у тебя всё получится😉"]

# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если нажали кнопку "➰Гороскоп"
    if message.text == "➰Гороскоп":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Готова? Сейчас я расскажу тебе гороскоп на сегодня.")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(text='♈Овен', callback_data='aries')
        # И добавляем кнопку на экран
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='♉Телец', callback_data='taurus')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='♊Близнецы', callback_data='gemini')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='♋Рак', callback_data='cancer')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='♌Лев', callback_data='leo')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='♍Дева', callback_data='virgo')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='♎Весы', callback_data='libra')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='♏Скорпион', callback_data='scorpio')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='♐Стрелец', callback_data='sagittarius')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='♑Козерог', callback_data='capricorn')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='♒Водолей', callback_data='aquarius')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='♓Рыбы', callback_data='pisces')
        keyboard.add(key_ryby)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
        
    # Если нажали кнопку "🎱Помогу принять решение" 
    if message.text == "🎱Помогу принять решение":
        bot.send_message(message.from_user.id, 'Хорошенько подумай о своём вопросе ко мне...')
        bot.send_message(message.from_user.id, 'Закрой глаза...')
        bot.send_message(message.from_user.id, 'Посчитай до 10...')
        keyboard = types.InlineKeyboardMarkup()
        key_next = types.InlineKeyboardButton(text='Далее➡', callback_data='quesion')
        keyboard.add(key_next)
        bot.send_message(message.from_user.id, text='Ты готова? 🤨', reply_markup=keyboard)
        
        
    elif message.text != "➰Гороскоп" and "🎱Помогу принять решение":
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Попробуй воспользоваться кнопками")
        
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "quesion":
        mesg = random.choice(first) + ' ' + random.choice(second)
        bot.send_message(call.message.chat.id, mesg)
    
    
    # Если нажали на одну из 12 кнопок — выводим гороскоп на день для знака зодиака нажатой кнопки
    if call.data != "quesion":
        sign = call.data
             
        URL = "https://www.marieclaire.ru/astro/%s/day/" % sign

        def parser(URL):
            r = requests.get(URL)
            soup = b(r.text, "html.parser")
            zodiac = soup.find_all("div", class_="block-text")
            return [c.text for c in zodiac]
        clear_zodiac = parser(URL)
            
        bot.send_message(call.message.chat.id, clear_zodiac)
# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)