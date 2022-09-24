import telebot
import random
from telebot import types
import requests
from bs4 import BeautifulSoup as b

bot = telebot.TeleBot('TOKEN')

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

# Заготовки для трёх предложений
first = ["Сегодня — идеальный день для новых начинаний.","Оптимальный день для того, чтобы решиться на смелый поступок!","Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.","Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.","Плодотворный день для того, чтобы разобраться с накопившимися делами."]
second = ["Но помните, что даже в этом случае нужно не забывать про","Если поедете за город, заранее подумайте про","Те, кто сегодня нацелен выполнить множество дел, должны помнить про","Если у вас упадок сил, обратите внимание на","Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]
second_add = ["отношения с друзьями и близкими.","работу и деловые вопросы, которые могут так некстати помешать планам.","себя и своё здоровье, иначе к вечеру возможен полный раздрай.","бытовые вопросы — особенно те, которые вы не доделали вчера.","отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]
third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.","Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.","Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.","Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.","Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]
fourth = ["Дорогая,", "Милая,", "Родная моя,", "Подруга,", "Драгоценная,", "Девочка,", ]
fifth = ["Лучше этого не делать", "Просто сделай это!", "Однозначно НЕТ", "Конечно же нет", "Да, да и ещё раз ДА!", "Сегодня лучше выпить винишка", "Подумай ещё", "В этой жизни нужно попровать всё, но неё это", "Попробуй ещё разок"]
sixth = []


# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "➰Гороскоп":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Готова? Сейчас я расскажу тебе гороскоп на сегодня.")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_next = types.InlineKeyboardButton(text='♈Овен', callback_data='zodiac')
        # И добавляем кнопку на экран
        keyboard.add(key_next)
        key_telec = types.InlineKeyboardButton(text='♉Телец', callback_data='zodiac')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='♊Близнецы', callback_data='zodiac')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='♋Рак', callback_data='zodiac')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='♌Лев', callback_data='zodiac')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='♍Дева', callback_data='zodiac')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='♎Весы', callback_data='zodiac')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='♏Скорпион', callback_data='zodiac')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='♐Стрелец', callback_data='zodiac')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='♑Козерог', callback_data='zodiac')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='♒Водолей', callback_data='zodiac')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='♓Рыбы', callback_data='zodiac')
        keyboard.add(key_ryby)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
        
        
    if message.text == "🎱Помогу принять решение":
        bot.send_message(message.from_user.id, "Хорошенько подумай о своём вопросе ко мне...")
        keyboard = types.InlineKeyboardMarkup()
        key_next = types.InlineKeyboardButton(text='Далее➡', callback_data='quesion')
        keyboard.add(key_next)
        bot.send_message(message.from_user.id, text='Готова?', reply_markup=keyboard)
        
        
    elif message.text != "➰Гороскоп" and "🎱Помогу принять решение":
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Попробуй воспользоваться кнопками")
        
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "zodiac": 
        # Формируем гороскоп
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    if call.data == "quesion": 
        mesg = random.choice(fourth) + ' ' + random.choice(fifth)
        bot.send_message(call.message.chat.id, mesg)
# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)