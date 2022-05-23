import time
import telebot
from telebot import types

import gitignore.tokens
from fitfood import racion
from fitfood import racion1

bot = telebot.TeleBot(gitignore.tokens.key)
users_clients = {}
users_recipes = {}
admin = 5041295792
last_time_message = {}


@bot.message_handler(commands=['start'])
def start_message(message):
    last_time_message[message.from_user.id] = int(time.time() // 1)  # антиспам защита
    # каждый раз, когда пользователь совершает действие, бот записывает текущее время и сравнивает его
    # с прошлым нажатием, если между ними прошло больше двух секунд, все хорошо, а если меньше - спам, программа просто не ответит
    users_clients[
        message.from_user.id] = []
    users_recipes[message.from_user.id] = ''
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Я готов(а)!🕺")
    markup.add(button1)
    if message.from_user.id == admin:
        bot.send_message(admin, 'Ожидаю ответа')
    else:
        bot.send_message(message.chat.id,
                         "Привет, с помощью этого бота ты сможешь стабилизировать вес и достичь желаемого результата!🐥",
                         reply_markup=markup),


@bot.message_handler(content_types='text')
def message_reply(message):
    global markup_imt_categories
    markup_imt_categories = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_days_of_the_week = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("<16")
    button2 = types.KeyboardButton("16-18,5")
    button3 = types.KeyboardButton("18,5-25")
    button4 = types.KeyboardButton("25-30")
    button5 = types.KeyboardButton("30-35")
    button6 = types.KeyboardButton("35-40")
    button7 = types.KeyboardButton(">40")

    button_mn = types.KeyboardButton("понедельник")
    button_ts = types.KeyboardButton("вторник")
    button_wd = types.KeyboardButton("среда")
    button_th = types.KeyboardButton("четверг")
    button_fr = types.KeyboardButton("пятница")
    button_st = types.KeyboardButton("суббота")
    button_sn = types.KeyboardButton("воскресенье")

    markup_imt_categories.add(button1, button2, button3, button4, button5, button6, button7)
    if message.text == "Я готов(а)!🕺":
        bot.send_message(message.chat.id,
                         'Для начала выберите число, полученное вами по этой формуле: m/h^2, где m — вес в килограммах, а h — рост в метрах. Таким образом мы сможем рассчитать ваш персональный индекс массы тела(ИМТ) и выявить вашу проблему🙂.',
                         reply_markup=markup_imt_categories)
    if message.text == '<16':
        if int(time.time() // 1) - last_time_message[message.from_user.id] < 2:
            return 0
        else:
            last_time_message[message.from_user.id] = int(time.time() // 1)
            markup_days_of_the_week.add(button_mn, button_ts, button_wd, button_th, button_fr, button_st, button_sn)
            msg = bot.send_message(message.chat.id,
                                   'У вас значительный дефицит массы тела😔. Вот ваш персональный рацион питания на неделю🥗🌮🌯!\n Выберите день недели:',
                                   reply_markup=markup_days_of_the_week)
            bot.register_next_step_handler(msg, show_deficit)
    if message.text == '16-18,5':
        if int(time.time() // 1) - last_time_message[message.from_user.id] < 2:
            return 0
        else:
            last_time_message[message.from_user.id] = int(time.time() // 1)
            markup_days_of_the_week.add(button_mn, button_ts, button_wd, button_th, button_fr, button_st, button_sn)
            msg = bot.send_message(message.chat.id,
                                   'У вас дефицит массы тела😕. Вот ваш персональный рацион питания на неделю🥗🌮🌯! Выберите текущий день недели:',
                                   reply_markup=markup_days_of_the_week)
            bot.register_next_step_handler(msg, show_deficit)
    if message.text == '18,5-25':
        if int(time.time() // 1) - last_time_message[message.from_user.id] < 2:
            return 0
        else:
            last_time_message[message.from_user.id] = int(time.time() // 1)
            bot.send_message(message.chat.id,
                             'Ваш вес в норме, у вас отличная фигура! Вы не нуждаетесь в нашей помощи! Но спасибо, что интересовались нами!😇😄',
                             reply_markup=markup_imt_categories)
    if message.text == '25-30':
        if int(time.time() // 1) - last_time_message[message.from_user.id] < 2:
            return 0
        else:
            last_time_message[message.from_user.id] = int(time.time() // 1)
            markup_days_of_the_week.add(button_mn, button_ts, button_wd, button_th, button_fr, button_st, button_sn)
            msg = bot.send_message(message.chat.id,
                                   'У вас есть лишний вес😕. Вот ваш персональный рацион питания на неделю🥗🌮🌯! Выберите текущий день недели:',
                                   reply_markup=markup_days_of_the_week)
            bot.register_next_step_handler(msg, show_excess)
    if message.text == '30-35':
        if int(time.time() // 1) - last_time_message[message.from_user.id] < 2:
            return 0
        else:
            last_time_message[message.from_user.id] = int(time.time() // 1)
            markup_days_of_the_week.add(button_mn, button_ts, button_wd, button_th, button_fr, button_st, button_sn)
            msg = bot.send_message(message.chat.id,
                                   'К сожалению, у вас ожирение первой степени. Не расстраивайтесь, мы поможем вам с этим справиться! Вот ваш персональный рацион питания на неделю🥗🌮🌯! Выберите текущий день недели:',
                                   reply_markup=markup_days_of_the_week)
            bot.register_next_step_handler(msg, show_excess)
    if (message.text == '35-40') or (message.text == '>40'):
        if int(time.time() // 1) - last_time_message[message.from_user.id] < 2:
            return 0
        else:
            last_time_message[message.from_user.id] = int(time.time() // 1)
            markup_days_of_the_week.add(button_mn, button_ts, button_wd, button_th, button_fr, button_st, button_sn)
            msg = bot.send_message(message.chat.id, 'К сожалению, у вас большой лишний вес. Но не расстраивайтесь, мы поможем вам с этим справиться! Вот ваш персональный рацион питания на неделю🥗🌮🌯! Выберите текущий день недели:', reply_markup=markup_days_of_the_week)
            bot.register_next_step_handler(msg, show_excess)


def show_deficit(message):
    if message.text == 'понедельник':
        bot.send_message(message.chat.id, racion('понедельник'), reply_markup=markup_imt_categories)
        bot.send_message(message.chat.id,
                         'Жизнь – это создание себя!😻 Чтобы начать, нужно перестать говорить и начать делать! Желаем вам удачи!')
    if message.text == 'вторник':
        bot.send_message(message.chat.id, racion('вторник'), reply_markup=markup_imt_categories)
    if message.text == 'среда':
        bot.send_message(message.chat.id, racion('среда'), reply_markup=markup_imt_categories)
        bot.send_message(message.chat.id,
                         'У вас обязательно получится достичь желаемого результата! Также не забывайте про спорт — это жизнь!🏃‍♀🏃‍♂ Если же все-таки возникнут проблемы, ваше моральное и физическое состояния ухудшатся, обратитесь обязательно к специалисту!')
    if message.text == 'четверг':
        bot.send_message(message.chat.id, racion('четверг'), reply_markup=markup_imt_categories)
    if message.text == 'пятница':
        bot.send_message(message.chat.id, racion('пятница'), reply_markup=markup_imt_categories)
        bot.send_message(message.chat.id, 'Главное — действовать!💯💥 Желаем вам удачи!')
    if message.text == 'суббота':
        bot.send_message(message.chat.id, racion('суббота'), reply_markup=markup_imt_categories)
    if message.text == 'воскресенье':
        bot.send_message(message.chat.id, racion('воскресенье'), reply_markup=markup_imt_categories)
        bot.send_message(message.chat.id, 'Мы верим в вас! Правильно поставленная цель уже наполовину достигнута!✅‼')


def show_excess(message):
    if message.text == 'понедельник':
        bot.send_message(message.chat.id, racion1('пн'), reply_markup=markup_imt_categories)
        bot.send_message(message.chat.id,
                         'Жизнь – это создание себя!💗 Чтобы начать, нужно перестать говорить и начать делать! Желаем вам удачи!')
    if message.text == 'вторник':
        bot.send_message(message.chat.id, racion1('вт'), reply_markup=markup_imt_categories)
    if message.text == 'среда':
        bot.send_message(message.chat.id, racion1('ср'), reply_markup=markup_imt_categories)
        bot.send_message(message.chat.id,
                         'У вас обязательно получится достичь желаемого результата! Также не забывайте про спорт — это жизнь!👣 Если же все-таки возникнут проблемы, ваше моральное и физическое состояния ухудшатся, обратитесь обязательно к специалисту!')
    if message.text == 'четверг':
        bot.send_message(message.chat.id, racion1('чт'), reply_markup=markup_imt_categories)
    if message.text == 'пятница':
        bot.send_message(message.chat.id, racion1('пт'), reply_markup=markup_imt_categories)
        bot.send_message(message.chat.id, 'Главное — действовать! Желаем вам удачи!💫💫💫')
    if message.text == 'суббота':
        bot.send_message(message.chat.id, racion1('сб'), reply_markup=markup_imt_categories)
    if message.text == 'воскресенье':
        bot.send_message(message.chat.id, racion1('вс'), reply_markup=markup_imt_categories)
        bot.send_message(message.chat.id,
                         'Мы верим в вас! Правильно поставленная цель уже наполовину достигнута!💪🏻🧠')


bot.infinity_polling()
