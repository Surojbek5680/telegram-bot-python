import telebot
import google.generativeai as genai

# 1. Bot tokeningizni kiriting (BotFather'dan olasiz)
TELEGRAM_TOKEN = '8615541607:AAFmP_J5t0eLczXhcPIBlOQpNF9326Esjqs'

# 2. Google Gemini API kalitini kiriting (aistudio.google.com dan olasiz)
GEMINI_API_KEY = 'AIzaSyDkEnep7mBJSp9Oucu_AO18fHZ0sYFAzDc'

# Gemini-ni sozlash
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men sun'iy intellektga ulangan botman. Menga xohlagan savolingizni bering!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        # Bot "yozmoqda..." holatini ko'rsatishi uchun
        bot.send_chat_action(message.chat.id, 'typing')
        
        # Savolni Gemini-ga yuboramiz
        response = model.generate_content(message.text)
        
        # Javobni foydalanuvchiga qaytaramiz
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Kechirasiz, xatolik yuz berdi. Keyinroq urinib ko'ring.")
        print(f"Xato: {e}")

print("Bot ishga tushdi...")
bot.polling()
