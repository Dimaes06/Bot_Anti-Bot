from telebot import *
from config import *
#from aiogram import *
from capt import *
import capt
from telebot.async_telebot import AsyncTeleBot
botAsync = AsyncTeleBot(token)

# bot = telebot.TeleBot('6271062258:AAH2iWQWdNWJnqIzST2onrYfASLWdsW1gn0')
bot = telebot.TeleBot(config.token)
chat_id = -1001501316623
# @bot.message_handler(commands=['dimaes'])
# def admin(message):

@bot.message_handler(commands=['start'])
def send_captcha(message):
    # Отправка капчи

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(config.emoji[p1], callback_data=str(config.animals[p1]))  #Создание кнопки
    btn2 = types.InlineKeyboardButton(config.emoji[p2], callback_data=str(config.animals[p2]))
    btn3 = types.InlineKeyboardButton(config.emoji[p3], callback_data=str(config.animals[p3]))
    btn4 = types.InlineKeyboardButton(config.emoji[p4], callback_data=str(config.animals[p4]))
    btn5 = types.InlineKeyboardButton(config.emoji[p5], callback_data=str(config.animals[p5]))
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    markup.row(btn5)
    captcha_image = open(config.animals[pic] + str(picNumb) + ".png", 'rb')  # Выбор рандомного животного и ранд тип
#    captcha_image = open(config.animals[4]+str(picNumb)+".png", 'rb')  # Замените 'captcha.png' на путь к вашей капче
    bot.send_message(message.chat.id, f'Определите животное на фото. На фото может быть\
 лишь художественное изображение животного')
    bot.send_photo(message.chat.id, captcha_image, reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_captcha(callback):

    if callback.data == capt.picL:
        bot.send_message(callback.message.chat.id, f'Верно! Доступ разрешен.')
        invite_link = bot.export_chat_invite_link(chat_id)
        bot.send_message(callback.message.chat.id, invite_link)

    elif callback.data == '':
        print('callback.data is null')
    else:
        bot.send_message(callback.message.chat.id, f'Неверный ответ. Попробуйте еще раз')

bot.polling(none_stop=True)
