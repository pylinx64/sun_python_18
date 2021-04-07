import telebot

bot = telebot.TeleBot('1710188888:AAG_fM6e1hF7pW6IAVhLCAYVjOhScuMpIhs')

@bot.message_handler(commands=['start'])
def start_text(message):
    print(message.chat.first_name, message.text)
    bot.send_message(message.chat.id, '🥡Привет, я чат-бот с колбасным тортом!')
    

    
print('#bot run...')
bot.polling()
