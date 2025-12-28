import os
import telebot
from gpt4free import g4f

# Берём токен из переменной окружения
TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    raise ValueError("⚠️ TELEGRAM_TOKEN не задан! Проверь настройки переменных окружения.")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])
def handle_message(message):
    # Если это группа или супергруппа, реагируем только на упоминания бота
    if message.chat.type in ["group", "supergroup"]:
        if bot.get_me().username.lower() not in message.text.lower():
            return

    try:
        # Отправляем текст пользователя в GPT
        response = g4f.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": message.text}]
        )
        bot.reply_to(message, response)
    except Exception as e:
        print("Ошибка при обработке сообщения:", e)
        bot.reply_to(message, "⚠️ Ошибка. Попробуй ещё раз.")

print("Bot is running...")
bot.infinity_polling()
