import telepot
import time
import random
import requests
from bs4 import BeautifulSoup as b
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


def construct_keyboard(data: list):
    keyboard_list = [[InlineKeyboardButton(text=item[0], callback_data=item[1])
                      for item in data_line]
                     for data_line in data]

    return InlineKeyboardMarkup(inline_keyboard=keyboard_list)


# Сообщение при старте бота. Можно поменять текст в тройных кавычках			
start_text = '''Привет, Дорогая!
Рада тебя видеть😘

P.S. Данный бот создан мужчиной для девушек и работает в тестовом режиме.dddd
Пока...
Посмотрим что из этого выйдет! ;-)
'''
# Заготовленный набор обращений (first) и ответов (second) для модуля принятия решения (magic_ball)
first = ["Дорогая,",
         "Милая,",
         "Родная моя,",
         "Подруга,",
         "Драгоценная,",
         "Девочка моя,",
         "Подружка,",
         "Прекрасная моя,",
         "Свет очей моих,"]

second = ["сейчас  у меня болит голова😰",
          "а карандаш был красный, или я опять не угадала?🙃",
          "Лучше этого не делать",
          "Просто сделай это!😎",
          "Однозначно НЕТ📛",
          "Конечно же нет",
          "Да, да и ещё раз ДА!😍",
          "Сегодня лучше выпить винишка🍷",
          "ещё разок подумай над вопросом",
          "42😱",
          "в этой жизни нужно попровать всё, кроме этого конечно",
          "Попробуй спросить ещё раз", "завтра, всё завтра...",
          "забудь пожалуйста об этом",
          "если это из-за него, то лучше перестань об этом думать",
          "давай не сейчас. Я слишком занята😵",
          "напишу как узнаю🙄",
          "ты самая крутая, у тебя всё получится😉"]


#Класс отвечающий за отправку рандомных, не повторяющихся, сообщений в разделе 'magic_ball'
class Message:
    def __init__(self):
        self.text = random.choice(first) + ' ' + random.choice(second)

    def new_message(self):
        self.text = random.choice(first) + ' ' + random.choice(second)
        return self.text

mesg = Message()

signs_q = {
        'data': construct_keyboard([[(u'Овен\U00002648 ', 'aries')],
                                    [(u'Телец\U00002649', 'taurus')],
                                    [(u'Близнецы\U0000264A', 'gemini')],
                                    [(u'Рак\U0000264B', 'cancer')],
                                    [(u'Лев\U0000264C', 'leo')],
                                    [(u'Дева\U0000264D', 'virgo')],
                                    [(u'Весы\U0000264E', 'libra')],
                                    [(u'Скорпион\U0000264F', 'scorpio')],
                                    [(u'Стрелец\U00002650', 'sagittarius')],
                                    [(u'Козерог\U00002651', 'capricorn')],
                                    [(u'Водолей\U00002652', 'aquarius')],
                                    [(u'Рыбы\U00002653', 'pisces')],
                                    [(u'\U00002B05 Назад', 'horoscope')],
                                    [(u'Главное меню', 'main_menu')]
                                    ]),
        'message_text': 'Выбери знак зодиака',
        'answer': None
    }


# Основная структура данных. Содержит состояние и соответствующие ему кнопки, текст и ответ
bot_data = {
    'main_menu': {
        'data': construct_keyboard([[(u"\U0001F52E Гороскоп", 'horoscope')],
                                    [(u'\U00002B50 Мотивация', 'motivation')],
                                    [(u'\U00002604 Новое', 'new_func')],
                                    [(u'\U0001F3B1 Помогу принять решение', 'magic_ball')],
                                    ]),
        'message_text': 'Выбери раздел',
        'answer': None
    },
    'horoscope': {
        'data': construct_keyboard([[(u'\U0001F4CC На день', 'day')],
                                    [(u'\U0001F5D3 На неделю', 'week')],
                                    [(u'\U0001F313 На месяц', 'month')],
                                    [(u'\U0001F407 На Год', 'year')],
                                    [(u'Назад', 'main_menu')]
                                    ]),

        'message_text': 'На сколько вы доверяете звёздам?',
        'answer': None
    },
    'motivation': {
        'data': construct_keyboard([[(u'\U0001F639 Для работы', 'joy_cat')],
                                    [(u'\U0001F63B Для учёбы', 'heart_eyes_cat')],
                                    [(u'\U0001F63C Для поступка', 'smirk_cat')],
                                    [(u'\U0001F63D Для самоуверенности', 'kissing_cat')],
                                    [(u'\U0001F640 Для поднятия настроения', 'scream_cat')],
                                    [(u'Назад', 'main_menu')
                                     ]]),
        'message_text': 'Мотивация для...',
        'answer': None
    },
    'new_func': {
        'data': construct_keyboard([[(u"\U0001F34E", 'red_apple'),
                                     (u"\U0001F34C", 'banana'),
                                     (u"\U0001F350", 'green_pear'),
                                     (u"\U0001F34B", 'yellow_lemon'),
                                     (u"\U0001F351", 'peach')],
                                    [('Назад', 'main_menu')]
                                    ]),
        'message_text': 'Выберите фрукт',
        'answer': None
    },
    'magic_ball': {
        'data': construct_keyboard([[('Я готова!', 'ready')]
                                    ]),
        'message_text': '''Чётко представь свой вопрос ко мне.        


Мысленно посчитай до пяти.
        
        
        
        
Ты готова?''',
        'answer': None,
    },

    'day': signs_q,
    'week': signs_q,
    'month': signs_q,
    'year': signs_q,

    'ready': {
        'data': construct_keyboard([
            [(u'Спросить ещё раз', 'magic_ball')],
            [(u'Назад', 'main_menu')]
        ]),
        'message_text': mesg.text,
        'answer': None,
    },
}

# Токен бота. Меняете бота -- меняете токен. Публично не выставлятЬ!
token = 

prev_state = {}
state = {'date': None,
	'sign': None,
}

#Функция-обработчик отправки текста в чат боту.
def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if chat_id not in prev_state:
        prev_state[chat_id] = None

    if prev_state[chat_id] is None:
        keyboard = construct_keyboard([[('Жми скорее!', 'main_menu')]])
        bot.sendMessage(chat_id=chat_id,
                        text=start_text,
                        reply_markup=keyboard)
    if prev_state[chat_id] != None:
        keyboard = construct_keyboard([[(u"\U0001F52E Гороскоп", 'horoscope')],
                                       [(u'\U00002B50 Мотивация', 'motivation')],
                                       [(u'\U00002604 Новое', 'new_func')],
                                       [(u'\U0001F3B1 Помогу принять решение', 'magic_ball')],
                                       ])
        bot.sendMessage(chat_id=chat_id,
                        text='Выбери раздел',
                        reply_markup=keyboard)


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg=msg,
                                                   flavor='callback_query')
    msg_id = msg['message']['message_id']
    react_to_query(from_id, msg_id, query_id, query_data)

#Функция парсер гороскопа из указанного URL
def parser(URL):
    r = requests.get(URL)
    soup = b(r.text, "html.parser")
    zodiac = soup.find_all("div", class_="block-text")
    return [c.text for c in zodiac]

#Функция генерации гороскопа в зависимости от нажатых кнопок 'sign' и 'date'
def generate_horoscope():
    URL = (f"https://www.marieclaire.ru/astro/{state['sign']}/{state['date']}/")
    
    clear_zodiac = parser(URL)
    print(state, clear_zodiac) #Для дебага
    return {
        'data': construct_keyboard([
            [(u'Назад', 'main_menu')]
        ]),
        'message_text': clear_zodiac,
        'answer': None,
    }

#Функция-обработчик наэатий кнопок
def react_to_query(chat_id, msg_id, query_id, query_data):
    bot.answerCallbackQuery(query_id, text='Click')
    prev_state[chat_id] = query_data
    bot_data['ready']['message_text'] = mesg.new_message()
    if query_data in bot_data:
        action = bot_data[query_data]
#Проверка нажимаемой кнопки. Если кнопки в разделе 'horoscope', запись значения query_data в переменную date
    if query_data in ('day', 'week', 'month', 'year'):
    	state['date'] = query_data
#Проверка нажимаемой кнопки. Если кнопки в разделе 'signs_q', запись значения query_data в переменную sign	
    elif query_data in ('aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 
                        'sagittarius', 'capricorn', 'aquarius', 'pisces'):
        state['sign'] = query_data
        action = generate_horoscope()
        
    data = action['data']
    text = action['message_text']
    bot.editMessageText(msg_identifier=(chat_id, msg_id),
        text=text,
    	reply_markup=data)

bot = telepot.Bot(token=token)

MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()

print('WARNING!!!', 'RoBot working...', 'Press CTRL+C to stop working (NOT RECOMENDED!)', sep='\n')

while 1:
    time.sleep(10)