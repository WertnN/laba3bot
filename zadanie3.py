import telebot

a = telebot.TeleBot("5219037251:AAHG1b3khSVSoicuRkYwZHgMkmGNX3Xuwfs")
keyboard = telebot.types.ReplyKeyboardMarkup(True) #наша клавиатура
keyboard.row("Да", "Нет")
name = '';
surname = '';
age = 0;

@a.message_handler(commands=['start'])
def startWork(message):
  tid = message.chat.id
  a.send_message(tid, "Давайте начнем!")
  a.send_message(tid, "Даля начала работы с ботом напишите /reg ")

@a.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        a.send_message(message.from_user.id, "Как тебя зовут?");
        a.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        a.send_message(message.from_user.id, 'Напиши /reg');

def get_name(message): #получаем фамилию
    global name;
    name = message.text;
    a.send_message(message.from_user.id, 'Какая у тебя фамилия?');
    a.register_next_step_handler(message, get_surname);

def get_surname(message):
    global surname;
    surname = message.text;
    a.send_message(message.from_user.id, 'Сколько тебе лет?');
    a.register_next_step_handler(message, get_age);

def get_age(message):
    global age;
    if age == 0: #проверяем что возраст изменился
        try:
            age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
            a.send_message(message.from_user.id, 'Цифрами, пожалуйста');

    question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?';
    a.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    a.register_next_step_handler(message, sendYourMessage);

def sendYourMessage(message):
    mid = message.chat.id
    if message.text == "Да":
        a.send_message(mid, "Запомню : )",reply_markup=telebot.types.ReplyKeyboardRemove())
        a.send_message(mid, "Если хочешь повторить напиши /reg")
    elif message.text =="Нет":
        a.send_message(mid, "Тогда напиши еще раз /reg",reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        a.send_message(mid, "Не правильные действия! Позязя напиши еще раз /reg : (")

a.polling()
