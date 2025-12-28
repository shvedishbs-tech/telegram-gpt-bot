import telebot
import os
from gpt4free import g4f

TOKEN = os.getenv("8202496303:AAHhfh3QEH6cA4z2g6zd48ZYZaEW9QmsZ0Y")

bot = telebot.TeleBot(8202496303:AAHhfh3QEH6cA4z2g6zd48ZYZaEW9QmsZ0Y)

@bot.message_handler(content_types=["text"])
def handle_message(message):
    if message.chat.type in ["group", "supergroup"]:
        if bot.get_me().username.lower() not in message.text.lower():
            return

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": message.text}]
        )
        bot.reply_to(message, response)
    except Exception:
        bot.reply_to(message, "⚠️ Ошибка. Попробуй ещё раз.")

print("Bot is running...")
bot.infinity_polling()
