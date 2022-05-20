#Импорт нужных нам библиотек
import time
import telebot
from telebot import types
from telebot.types import LabeledPrice
import ffood
from ffood import *
import re

bot = telebot.TeleBot('5041295792:AAHnZp6OTtCazXslXuwxNLnTCvvJrxg9bAo')
users_clients = {}
users_recipes = {}
admin = 5041295792
last_time_message = {}


@bot.message_handler(commands=['start'])
def start_message(message):
    last_time_message[message.from_user.id] = int(time.time() // 1) #антиспам защита
    #каждый раз, когда пользователь совершает действие, бот записывает текущее время и сравнивает его
    #с прошлым нажатием, если между ними прошло больше двух секунд, все хорошо, а если меньше - спам, программа просто не ответит
    users_clients[message.from_user.id] = [] #дальше в три строки вместе с этой записывается айдишник пользователь НЕ НУЖНО!!!!!!
    users_recipes[message.from_user.id] = ''
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Я готов(а)!🕺")
    markup.add(button1)
    if message.from_user.id == admin:
        bot.send_message(admin, 'Ожидаю ответа')
    else:
        bot.send_message(message.chat.id, "Привет, с помощью этого бота ты сможешь стабилизировать вес и достичь желаемого результата!", reply_markup=markup),


@bot.message_handler(content_types='text')
def message_reply(message):
    global markup_imt_categories
    markup_imt_categories = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("<16")
    button2 = types.KeyboardButton("16-18,5")
    button3 = types.KeyboardButton("18,5-25")
    button4 = types.KeyboardButton("25-30")
    button5 = types.KeyboardButton("30-35")
    button6 = types.KeyboardButton("35-40")
    button7 = types.KeyboardButton(">40")
    markup_imt_categories.add(button1, button2, button3, button4, button5, button6, button7)
    if message.text == "Я готов(а)!🕺":
        bot.send_message(message.chat.id, 'Для начала выберите число, полученное вами по этой формуле: m/h^2, где m — вес в килограммах, а h — рост в метрах. Таким образом мы сможем рассчитать ваш персональный индекс массы тела(ИМТ) и выявить вашу проблему🙂.', reply_markup=markup_imt_categories)
    if message.text == '<16': #НЕТ РЕЦЕПТА ДЛЯ НАБОРА ВЕСА!!!!!!!!!!!!!!!!!!!!
        if int(time.time() // 1) - last_time_message[message.from_user.id] < 2:
            return 0
        else:
            last_time_message[message.from_user.id] = int(time.time() // 1)
            bot.send_message(message.chat.id, 'У вас значительный дефицит массы тела😔. Вот ваш персональный рацион питания на неделю🥗🌮🌯!', reply_markup=markup_imt_categories)
    if message.text == '16-18,5':
        if int(time.time() // 1) - last_time_message[message.from_user.id] < 2:
            return 0
        else:
            last_time_message[message.from_user.id] = int(time.time() // 1)
            bot.send_message(message.chat.id, 'У вас дефицит массы тела😕. Вот ваш персональный рацион питания на неделю🥗🌮🌯!', reply_markup=markup_imt_categories)
    if message.text == '18,5-25':
        if int(time.time() // 1) - last_time_message[message.from_user.id] < 2:
            return 0
        else:
            last_time_message[message.from_user.id] = int(time.time() // 1)
            bot.send_message(message.chat.id, 'Ваш вес в норме, у вас отличная фигура! Вы не нуждаетесь в нашей помощи! Но спасибо, что интересовались нами!😇😄' , reply_markup=markup_imt_categories)
    if message.text == '25-30':
        if int(time.time() // 1) - last_time_message[message.from_user.id] < 2:
            return 0
        else:
            last_time_message[message.from_user.id] = int(time.time() // 1)
            bot.send_message(message.chat.id, 'У вас есть лишний вес😕. Вот ваш персональный рацион питания на неделю🥗🌮🌯!', reply_markup=markup_imt_categories)
    if message.text == '30-35':
        if int(time.time() // 1) - last_time_message[message.from_user.id] < 2:
            return 0
        else:
            last_time_message[message.from_user.id] = int(time.time() // 1)
            bot.send_message(message.chat.id, 'К сожалению, у вас ожирение первой степени. Не расстраивайтесь, мы поможем вам с этим справиться! Вот ваш персональный рацион питания на неделю🥗🌮🌯!', reply_markup=markup_imt_categories)
    if (message.text == '35-40') or (message.text == '>40'):
        if int(time.time() // 1) - last_time_message[message.from_user.id] < 2:
            return 0
        else:
            last_time_message[message.from_user.id] = int(time.time() // 1)
            bot.send_message(message.chat.id, 'К сожалению, у вас большой лишний вес. Но не расстраивайтесь, мы поможем вам с этим справиться! Вот ваш персональный рацион питания на неделю🥗🌮🌯!', reply_markup=markup_imt_categories)

@bot.message_handler(content_types='answer')
def mesage_support(message):
    global markup_answer
    markup_answer = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Спасибо! Буду придерживаться этому рациону!🕺😋🥰")
    button2 = types.KeyboardButton("Замечательно! Надеюсь, смогу преодолеть свою проблему!")
    markup_answer.add(button1, button2)
    if message.answer == 'Спасибо! Буду придерживаться этому рациону!🕺😋🥰':
        if int(time.time() // 1) - last_time_message[message.from_user.id] < 2:
            return 0
        else:
            last_time_message[message.from_user.id] = int(time.time() // 1)
            bot.send_message(message.chat.id, 'Мы очень рады! У вас обязательно все получится, мы верим в вас! Также не забывайте про спорт — это жизнь! Если же все-таки возникнут проблемы, ваше моральное и физическое состояния ухудшатся, обратитесь обязательно к специалисту! Желаем вам удачи!', reply_markup=markup_answer)
    if message.answer == 'Замечательно! Надеюсь, смогу преодолеть свою проблему!':
        if int(time.time() // 1) - last_time_message[message.from_user.id] < 2:
            return 0
        else:
            last_time_message[message.from_user.id] = int(time.time() // 1)
            bot.send_message(message.chat.id, 'У вас обязательно получится достичь желаемого результата! Главное — действовать! Также не забывайте про спорт — это жизнь! Если же все-таки возникнут проблемы, ваше моральное и физическое состояния ухудшатся, обратитесь обязательно к специалисту! Желаем вам удачи!', reply_markup=markup_answer)

bot.infinity_polling() #включаем бота
