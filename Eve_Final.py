import telebot
import types
from telebot import types

bot = telebot.TeleBot('2058161307:AAE3Txv8-P1aHzIbzJdIN3fbbIvUOXm7GOs')

name, surname, age, level = ('', '',0, 0)



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id,"Привет, это EveBot")
    mainmenu = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    
    mainmenu.add(key_yes, key_no)
    bot.send_message(message.chat.id, 'Желаете ли вы зарегистрироваться, чтобы впоследствии получать уведомления о мероприятиях?',
                     reply_markup=mainmenu)


@bot.callback_query_handler(lambda call: call.data in ["yes", "no"])
def callback_worker1(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id,
                         "Давай познакомимся! Как тебя зовут?")
        bot.register_next_step_handler(call.message, reg_name)
        return
    elif call.data == "no":
        bot.send_message(call.message.chat.id,"Выбери в меню, что бы ты хотел найти")
        

def reg_name(message):
    global name
    name = message.text
    if name.isalpha():
        bot.send_message(message.from_user.id, "Какая у тебя фамилия?")
        bot.register_next_step_handler(
            message, reg_surname)  # получаем фамилию
    else:
        bot.send_message(message.from_user.id, "Вводите буквами")
        # проверка на правильно введение
        bot.register_next_step_handler(message, reg_name)


def reg_surname(message):
    global surname
    surname = message.text
    if surname.isalpha():
        bot.send_message(message.from_user.id, "Понял, принял! Теперь укажи, пожалуйста, свой возраст.")
        bot.register_next_step_handler(
            message, reg_age)  # получаем класс ученика
    else:
        bot.send_message(message.from_user.id, "Попробуй еще раз")
        # проверка на правильно введение
        bot.register_next_step_handler(message, reg_surname)

def reg_age(message):
    global age
    age = message.text
    if age.isdigit():
        age = int(age)
        if age>0 and age<=18:
            bot.send_message(message.chat.id, "Зафиксировал, теперь укажи в каком ты классе")
            bot.register_next_step_handler(
            message, reg_level)# получаем класс ученика
        elif age>18 and age<100:
            bot.send_message(message.chat.id, "Зафиксировал")

        else:
            bot.send_message(message.chat.id, "Не верю! Попробуй еще раз")
            bot.register_next_step_handler(
            message, reg_age)  # получаем  возраст
    else:
        bot.send_message(message.chat.id, "Не верю! Попробуй еще раз")
        bot.register_next_step_handler(
        message, reg_age)  # получаем  возраст
      
def reg_level(message):
    global level
    level = message.text
    if level in ['5', '6', '7', '8', '9', '10', '11'] :
        bot.send_message(message.from_user.id, "Понял, принял")
    else:
        bot.send_message(message.from_user.id,
                         "Нет нет, так не прокатит). Впиши цифру своего класса от 5 до 11)")
        # проверка на правильно введение
        bot.register_next_step_handler(message, reg_level)

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yess')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='noo')
    keyboard.add(key_no)
    question = 'Ты в ' + str(level) + \
        ' классе? И тебя зовут: ' + name + ' ' + surname + '?'
    bot.send_message(message.from_user.id, text=question,
                     reply_markup=keyboard)  # уточняем верны ли данные пользователя


@bot.callback_query_handler(lambda query: query.data in ["yess", "noo"])
def callback_worker(query):
    try:
        if query.data == "yess":
            bot.send_message(
                query.message.chat.id, "Приятно познакомиться! А теберь выбери в меню, что тебя интересует")
        elif query.data == "noo":
            # повторное введение данных
            bot.send_message(query.message.chat.id, "Попробуем еще раз!")
            bot.send_message(query.message.chat.id,
                             "Привет! Давай познакомимся! Как тебя зовут?")
            bot.register_next_step_handler(query.message, reg_name)
    except Exception as e:
        print(repr(e))

@bot.message_handler(commands=['events'])#мероприятия
def inline_eve(message):
    vent = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Краснодар", callback_data="Krasnodar")
    but_2 = types.InlineKeyboardButton(text="Казань", callback_data="Kazan")
    but_3 = types.InlineKeyboardButton(text="Москва", callback_data="Moscow")
    vent.add(but_1, but_2, but_3)
    bot.send_message(message.chat.id, "Выберите ваш город:", reply_markup=vent)

@bot.callback_query_handler(lambda query: query.data in ["Krasnodar", "Kazan","Moscow"])
def inline(call):
    try:
        if call.data == "Moscow":
            bot.send_message(call.message.chat.id, "Лови список:")
            bot.send_message(call.message.chat.id, "XV Большой фестиваль мультфильмов")
            bot.send_message(call.message.chat.id, "2021-10-28")
            bot.send_message(call.message.chat.id, "Многие помнят, какими яркими и душевными были советские мультфильмы. Но что актуально в данный момент, какие новые работы выпускают ведущие анимационные студии и художники? Посмотреть лучшие работы отечественных и зарубежных авторов можно будет на XV фестивале мультфильмов.")
            bot.send_message(call.message.chat.id, "https://kudago.com/msk/event/festival-bolshoj-festival-multfilmov/")
            bot.send_message(call.message.chat.id, "Фестиваль Matrëshka-Market Fest")
            bot.send_message(call.message.chat.id, "2021-12-11")
            bot.send_message(call.message.chat.id, "Ароматные свечи, уютные вязаные вещи, необычные украшения, стильная посуда и элементы декора, милые детские вещи ждут вас на фестивале Matrëshka-Market Fest. Все вещи, которые выставят на продажу на ярмарке, созданы творческими людьми, настоящими мастерами своего дела.")
            bot.send_message(call.message.chat.id, "https://kudago.com/msk/event/festival-matrshka-market-fest/")
        elif call.data == "Kazan":
            bot.send_message(call.message.chat.id, "Лови список:")
    except Exception as e:
        print(repr(e))

@bot.message_handler(commands=['olympiads'])
def inline_key(message): 
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Обществознание', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='Биология', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='Математика', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Химия', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='Информатика', callback_data=5))
    markup.add(telebot.types.InlineKeyboardButton(text='История', callback_data=6))
    markup.add(telebot.types.InlineKeyboardButton(text='Инженерные науки', callback_data=7))
    markup.add(telebot.types.InlineKeyboardButton(text='Естественные науки', callback_data=8))
    markup.add(telebot.types.InlineKeyboardButton(text='География', callback_data=9))
    markup.add(telebot.types.InlineKeyboardButton(text='Физика', callback_data=10))

    bot.send_message(message.chat.id,  message.from_user.first_name + ', выбери направление', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Минуточку, готовлю список!')
    if call.data in ['1','2','3','4','5','6','7','8','9','10']:
        key = types.InlineKeyboardMarkup()
        but_1 = types.InlineKeyboardButton(text="1", callback_data="11")
        but_2 = types.InlineKeyboardButton(text="2", callback_data="12")
        but_3 = types.InlineKeyboardButton(text="3", callback_data="13")
        key.add(but_1, but_2, but_3)
        bot.send_message(call.message.chat.id, 'Выбери уровень олимпиады', reply_markup=key)
    


@bot.message_handler(commands=['competitions'])
def compet_message(message):
    mainmen = types.InlineKeyboardMarkup(resize_keyboard = True)
    con1 = types.InlineKeyboardButton(text=' Инженерные ', callback_data='con1')
    con2 = types.InlineKeyboardButton(text='Творческие', callback_data='con2')
    con3 = types.InlineKeyboardButton(text='Для предпринимателей', callback_data='con3')
    con4 = types.InlineKeyboardButton(text='Естественные науки', callback_data='con4')
    
    mainmen.add(con1 , con2, con3, con4)
    bot.send_message(message.chat.id, message.from_user.first_name  + 'Выбери направление конкурсов',
                     reply_markup=mainmen)  # выбор направлений

@bot.callback_query_handler(lambda query: query.data in ["con1", "con2","con3","con4"])
def query_handler(d):
        if d.data in ['con1','con2','con3','con4']:
            bot.send_message(d.message.chat.id, 'Вот держи список')
    

@bot.message_handler(commands=['volunteer'])
def inline_vol(message):
    key = types.InlineKeyboardMarkup()
    vol1 = types.InlineKeyboardButton(text="Помощь детям", callback_data="vol1")
    vol2 = types.InlineKeyboardButton(text="Помощь взрослым", callback_data="vol2")
    vol3 = types.InlineKeyboardButton(text="Помощь пожилым", callback_data="vol3")
    vol4 = types.InlineKeyboardButton(text="Помощь в проведении патриотических мероприятий", callback_data="vol4")
    vol5 = types.InlineKeyboardButton(text="Помощь в чрезвычайных ситуациях", callback_data="vol5")
    vol6 = types.InlineKeyboardButton(text="Помощь в защите культурного наследия ", callback_data="vol6")
    key.add(vol1, vol2, vol3 , vol4, vol5, vol6)
    bot.send_message(message.chat.id, "Выберите тип волонтерского мероприятия", reply_markup=key)

@bot.callback_query_handler(lambda query: query.data in ['vol1', 'vol2', 'vol3' , 'vol4', 'vol5', 'vol6'])
def inline_n(v):
  if v.data in ['vol1', 'vol2', 'vol3' , 'vol4', 'vol5', 'vol6']:
    bot.send_message(v.message.chat.id, v.message.from_user.first_name  + 'Лови список мероприятий')



# в случае введения команды, которую бот не может распознать
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, " Извини, я не понял твою команду(")


try: 
    bot.polling(none_stop=True, interval=0)
except Exception:
    pass


