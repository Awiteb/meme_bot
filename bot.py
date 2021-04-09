# -*- coding: utf-8 -*-
import telebot
import requests
from time import sleep

"""
 Developed by: Awiteb       |
 GitHub: Awiteb             |
 Email: Awiteb@hotmail.com  |
"""
with open('botToken.txt', 'r') as f:
    token = f.read()
bot = telebot.TeleBot(token=token.strip('\n'))
meme_api = "https://meme-api.herokuapp.com/gimme"

start_message = f"""
مرحبا،
أنا @{bot.get_me().username} روبوت بسيط لإرسال الميمز في مجموعة أو دردشة خاصة
طريقة طلب الميمز بسيطة ، فقط أرسل /get_meme@{bot.get_me().username}

Hi,
I'm @{bot.get_me().username} simple bot to send meme in group or private messages
The way to request a meme is simple,
just send /get_meme@{bot.get_me().username}
"""

# Function to get memes
def get_meme(message):
    meme_data = requests.get(meme_api).json()
    meme_img = meme_data["preview"][-1]
    photo = requests.get(meme_img).content
    bot.send_chat_action(message.chat.id, 'upload_photo')
    bot.send_photo(message.chat.id, photo,reply_to_message_id= message.id,caption=meme_data['title'])


@bot.message_handler(commands=['start','help','get_meme'])
def commands_handler(message):
    text = str(message.text)
    # if user requests meme
    if text.startswith('/get_meme'):
        get_meme(message)
    # else
    else:
        bot.reply_to(message, start_message)    

if __name__ == "__main__":
    while True:
        try:
            print(f"@{bot.get_me().username}")
            print("start bot")
            bot.polling()
        except Exception as e :
            print(e)
            sleep(15)
