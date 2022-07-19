import telepot
import time
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

# Если машина находится в России и на машине не настроены прокси 
# можно раскомментить эту строку и подставить адрес публичного прокси-сервера

#telepot.api.set_proxy("http://100.39.36.100:35531")


def construct_keyboard(data: list):
    keyboard_list = [[InlineKeyboardButton(text=item[0], callback_data=item[1])
                      for item in data_line]
                     for data_line in data]

    return InlineKeyboardMarkup(inline_keyboard=keyboard_list)


'''
TODO
Пофиксить хардкод
'''
emoji_sq = (u'\U0001F639' + u'\U0001F499' + u"\U0001F32A" + u"\U0001F34B" +
            u"\U0001F34C" + u'\U0001F49C' + u'\U0001F63B' + u"\U0001F4A7" +
            u"\U00002744" + u"\U000026A1" + u"\U0001F63C" + u'\U00002764' +
            u"\U0001F640" + u"\U0001F63D" + u"\U0001F350" + u'\U0001F49A' +
            u'\U0001F49B' + u"\U0001F351" + u"\U0001F525" + u"\U0001F34E")

			
# Сообщение при старте игры. Можно поменять текст в тройных кавычках			
start_text = '''Всем привет, дорогие друзья! 
Приветствую вас на квест-игре Telegram "School"!
Для прохождения игры вам необходимо получить финальный код, ответив на все вопросы, закодированные в виде QR-кода. 
QR-коды расположены по территории, разгадав головоломку впишите правильный ответ в нужную категорию и получите часть финального кода. 
Собрав все части кода, объедините их в правильной последовательности и введите его в разделе "Окончание игры"
'''

# Сообщение перед проверкой финального кода
final_check_message = '''Впишите финальный код в правильном порядке (без пробелов) и отправьте.\n
Каждой картинке соответствует полученный вами код.\n''' + emoji_sq

good_answer_pattern = 'Правильно! Часть кода замка на выход - '
bad_answer_pattern = 'Неправильно! Пробуйте еще!'


# Сообщение конца игры. Можно поменять текст в тройных кавычках	
game_over_message = '''Поздравляю!!! Вы прошли игру квест-игру Telegram "School". 
Заберите заслуженный приз у ведущего игры и продолжайте в том же духе! 
До новых встреч!'''


# Основная структура данных. Содержит состояние и соответствующие ему кнопки, текст и ответ
quiz_data = {
    'main_menu': {
        'data': construct_keyboard([[(u"\U0001F49F", 'heart_category'),
                                     (u'\U0001F63A', 'cat_category'),
                                     (u'\U0001F34F', 'fruit_category'),
                                     (u'\U00002600', 'weather_category')],
                                    [('Окончить игру', 'end_game')]
                                    ]),
        'message_text': 'Выберите категорию',
        'answer': None
    },
    'heart_category': {
        'data': construct_keyboard([[(u'\U00002764', 'red_heart'),
                                     (u'\U0001F499', 'blue_heart'),
                                     (u'\U0001F49A', 'green_heart'),
                                     (u'\U0001F49B', 'yellow_heart'),
                                     (u'\U0001F49C', 'purple_heart')],
                                    [(u'Назад', 'main_menu')]
                                    ]),
        'message_text': 'Выберите цвет сердца',
        'answer': None
    },
    'cat_category': {
        'data': construct_keyboard([[(u'\U0001F639', 'joy_cat'),
                                     (u'\U0001F63B', 'heart_eyes_cat'),
                                     (u"\U0001F63C", 'smirk_cat'),
                                     (u"\U0001F63D", 'kissing_cat'),
                                     (u"\U0001F640", 'scream_cat')],
                                    [(u'Назад', 'main_menu')
                                     ]]),
        'message_text': 'Выберите смайлик с котиком',
        'answer': None
    },
    'fruit_category': {
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
    'weather_category': {
        'data': construct_keyboard([[(u"\U000026A1", 'lightning'),
                                     (u"\U0001F525", 'flame'),
                                     (u"\U0001F4A7", 'water'),
                                     (u"\U00002744", 'snowflake'),
                                     (u"\U0001F32A", 'tornado')],
                                    [('Назад', 'main_menu')]
                                    ]),
        'message_text': 'Выберите природное явление',
        'answer': None
    },
    'red_apple': {
        'data': None,
        'message_text': 'Какой ответ у вопроса под картинкой красным яблоком?',
        'answer': '11',
        'right_answer': good_answer_pattern + '25',
        'wrong_answer': bad_answer_pattern
    },
    'banana': {
        'data': None,
        'message_text': 'Какой ответ у вопроса под картинкой с бананом?',
        'answer': 'король',
        'right_answer': good_answer_pattern + '08',
        'wrong_answer': bad_answer_pattern
    },
    'green_pear': {
        'data': None,
        'message_text': 'Какой ответ у вопроса под картинкой с грушей?',
        'answer': '72',
        'right_answer': good_answer_pattern + '99',
        'wrong_answer': bad_answer_pattern
    },
    'yellow_lemon': {
        'data': None,
        'message_text': 'Какой ответ у вопроса под картинкой с лимоном?',
        'answer': 'верхние',
        'right_answer': good_answer_pattern + '76',
        'wrong_answer': bad_answer_pattern
    },
    'peach': {
        'data': None,
        'message_text': 'Какой ответ у вопроса, скрывающегося под персиком?',
        'answer': 'саша',
        'right_answer': good_answer_pattern + '84',
        'wrong_answer': bad_answer_pattern
    },
    'red_heart': {
        'data': None,
        'message_text': 'Какой ответ у вопроса под красным сердечком?',
        'answer': '2',
        'right_answer': good_answer_pattern + '65',
        'wrong_answer': bad_answer_pattern
    },
    'blue_heart': {
        'data': None,
        'message_text': 'Какой ответ у вопроса под синим сердечком?',
        'answer': '$5000',
        'right_answer': good_answer_pattern + '12',
        'wrong_answer': bad_answer_pattern
    },
    'green_heart': {
        'data': None,
        'message_text': 'Какой ответ у вопроса под зеленым сердечком?',
        'answer': '6',
        'right_answer': good_answer_pattern + '56',
        'wrong_answer': bad_answer_pattern
    },
    'yellow_heart': {
        'data': None,
        'message_text': 'Какой ответ у вопроса под желтым сердечком?',
        'answer': 'сегодня',
        'right_answer': good_answer_pattern + '35',
        'wrong_answer': bad_answer_pattern
    },
    'purple_heart': {
        'data': None,
        'message_text': 'Какой ответ у вопроса под фиолетовым сердечком?',
        'answer': 'а',
        'right_answer': good_answer_pattern + '78',
        'wrong_answer': bad_answer_pattern
    },
    'lightning': {
        'data': None,
        'message_text': 'Какой ответ у вопроса, скрытого под молнией?',
        'answer': 'проходная',
        'right_answer': good_answer_pattern + '32',
        'wrong_answer': bad_answer_pattern
    },
    'flame': {
        'data': None,
        'message_text': 'Какой ответ у вопроса, скрытого под пламенем?',
        'answer': 'ноги',
        'right_answer': good_answer_pattern + '80',
        'wrong_answer': bad_answer_pattern
    },
    'water': {
        'data': None,
        'message_text': 'Какой ответ у вопроса, скрытого под символом воды?',
        'answer': 'закладка',
        'right_answer': good_answer_pattern + '71',
        'wrong_answer': bad_answer_pattern
    },
    'snowflake': {
        'data': None,
        'message_text': 'Какой ответ у вопроса, скрытого под снежинкой?',
        'answer': 'чай',
        'right_answer': good_answer_pattern + '95',
        'wrong_answer': bad_answer_pattern
    },
    'tornado': {
        'data': None,
        'message_text': 'Какой ответ у вопроса, скрытого под торнадо?',
        'answer': 'велосипед',
        'right_answer': good_answer_pattern + '03',
        'wrong_answer': bad_answer_pattern
    },
    'joy_cat': {
        'data': None,
        'message_text': 'Напишите ответ на вопрос задорно смеющегося котика',
        'answer': 'почта',
        'right_answer': good_answer_pattern + '00',
        'wrong_answer': bad_answer_pattern
    },
    'heart_eyes_cat': {
        'data': None,
        'message_text': 'Напишите ответ на вопрос влюбленного котика',
        'answer': 'йогурт',
        'right_answer': good_answer_pattern + '10',
        'wrong_answer': bad_answer_pattern
    },
    'smirk_cat': {
        'data': None,
        'message_text': 'Какой же ответ у вопроса ухмыляющегося котика?',
        'answer': 'саксофон',
        'right_answer': good_answer_pattern + '51',
        'wrong_answer': bad_answer_pattern
    },
    'kissing_cat': {
        'data': None,
        'message_text': 'Напишите ответ на вопрос котика-целовашки',
        'answer': 'трамвай',
        'right_answer': good_answer_pattern + '83',
        'wrong_answer': bad_answer_pattern
    },
    'scream_cat': {
        'data': None,
        'message_text': 'Напишите ответ на вопрос испуганного котейки',
        'answer': 'сапоги',
        'right_answer': good_answer_pattern + '43',
        'wrong_answer': bad_answer_pattern
    },
    'end_game': {
        'data': None,
        'message_text': final_check_message,
        'answer': '0012037608781071953251654383995635848025',
        'right_answer': game_over_message,
        'wrong_answer': bad_answer_pattern
    }
}


# Токен бота. Меняете бота -- меняете токен. Публично не выставлятЬ!
token = "707090423:AAEwUb6h8cLsKandDjIoW4PxvNp__KsDsa0"
# token = "652391787:AAGJnMAHNZ6hPh2eAzBjheVpof5oXZbED2w"

prev_state = {}


def get_answer(msg):
    msg_text = str(msg['text'])
    return msg_text.lower().strip().replace(' ', '')


def is_correct_answer(user_answer, ethalon):
    return user_answer == ethalon


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if chat_id not in prev_state:
        prev_state[chat_id] = None

    if prev_state[chat_id] is None:
        keyboard = construct_keyboard([[('Начать игру!', 'main_menu')]])
        bot.sendMessage(chat_id=chat_id,
                        text=start_text,
                        reply_markup=keyboard)

    elif 'right_answer' in quiz_data[prev_state[chat_id]]:
        answer = get_answer(msg)
        keyboard = construct_keyboard([[('Главное меню', 'main_menu')]])
        if is_correct_answer(answer, quiz_data[prev_state[chat_id]]['answer']):
            message_text = quiz_data[prev_state[chat_id]]['right_answer']
        else:
            message_text = quiz_data[prev_state[chat_id]]['wrong_answer']
        bot.sendMessage(chat_id=chat_id,
                        text=message_text,
                        reply_markup=keyboard)
    else:
        data = quiz_data[prev_state[chat_id]]['data']
        text = quiz_data[prev_state[chat_id]]['message_text']
        bot.sendMessage(chat_id=chat_id,
                        text=text,
                        reply_markup=data)


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg=msg,
                                                   flavor='callback_query')
    msg_id = msg['message']['message_id']
    react_to_query(from_id, msg_id, query_id, query_data)


def react_to_query(chat_id, msg_id, query_id, query_data):
    bot.answerCallbackQuery(query_id, text='Got it')
    prev_state[chat_id] = query_data

    for state in quiz_data:
        if state == query_data:
            data = quiz_data[state]['data']
            text = quiz_data[state]['message_text']
            bot.editMessageText(msg_identifier=(chat_id, msg_id),
                                text=text,
                                reply_markup=data)


bot = telepot.Bot(token=token)

MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)
