
import telebot

# токен
bot = telebot.TeleBot('1710188888:AAG_fM6e1hF7pW6IAVhLCAYVjOhScuMpIhs')

@bot.message_handler(commands=['start'])
def start_text(message):
    print(message.chat.first_name, message.text)
    bot.send_message(message.chat.id, '🥡Привет, я чат-бот с колбасным тортом!')
    
@bot.message_handler(content_types=['text'])
def message_text(message):
    # отправляет сообщение
    if message.text == 'привет':
        bot.send_message(message.chat.id, 'Ну хай')
    else:
        bot.send_message(message.chat.id, 'Я тебя не понял')
    
print('#bot run...')
bot.polling()
