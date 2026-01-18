import telebot
from flask import Flask
from threading import Thread

# سيرفر وهمي لضمان بقاء البوت نشطاً على Render
app = Flask('')
@app.route('/')
def home(): 
    return "Bot is Running!"

def run(): 
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

TOKEN = '8538111354:AAFNBBjSC9fUCEXD1G3RKGETupS9_VUeTsk'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلاً بك! تم تفعيل البوت بنجاح على السحابة ☁️ سأعمل الآن 24 ساعة دون انقطاع.")

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
