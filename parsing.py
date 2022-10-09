#   Перед импортом библиотек нужно в командной строке (терминале) выполнить команды:
#   pip(pip3 если у Вас Linux) install requests
#   pip(pip3 если у Вас Linux) install bs4


import requests                                                 #импорт библиотеки для работы с HTTP/HTTPS запросами
from bs4 import BeautifulSoup as b                              #импорт библиотеки BeautifulSoup в константу b (для сокращения дальнейшего кода)

sign = 'libra'                                                  #значение переменной sign
date = 'day'                                                    #значение переменной date

URL = (f"https://www.elle.ru/astro/{sign}/{date}/")             #Исходный URL с которого парсим, с помощью (f"...") подставляем переменные в строку

def parser(URL):                                                #Функция парсинга, принимает на вход URL
    r = requests.get(URL)                                       #GET запрос к URL
    soup = b(r.text, "html.parser")                             #Выгрузка текста со страницы
    zodiac = soup.find_all("div", class_="articleParagraph")    #Откуда выгрузка, указание блока "div" и класса "articleParagraph"
    return [c.text for c in zodiac]                             #Очистка ненужного содержимого из результата парсинга
clear_zodiac = parser(URL)                                      #Запись в переменную результатов выполнения функции парсинга
print(clear_zodiac)                                             #Печать в консоль содержимого переменной