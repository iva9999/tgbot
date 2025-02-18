import telebot
from task import gen_pass
token = 'token'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.send_message(message.chat.id, "Пока! Удачи!")
    
@bot.message_handler(commands=['image'])
def send_bye(message):
    with open("cat.jpg", "rb") as file:
        
        bot.send_photo(message.chat.id, file)

@bot.message_handler(commands=['pass'])
def send_pass(message):
    bot.send_message(message.chat.id, gen_pass(10))
    
 # Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)




print('botstart')
bot.polling()
