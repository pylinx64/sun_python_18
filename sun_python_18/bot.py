import telebot

# токен
bot = telebot.TeleBot('1710188888:AAG_fM6e1hF7pW6IAVhLCAYVjOhScuMpIhs')

#-----------------------------start-------------------------------------
@bot.message_handler(commands=['start'])
def start_text(message):
    # консоль. Выводит на экран кто/что написал
    print(message.chat.first_name, message.text)
    # отправляет сообщение бот
    bot.send_message(message.chat.id, '🥡Привет, я чат-бот с колбасным тортом!')
#-----------------------------start-------------------------------------

#-----------------------------text--------------------------------------
@bot.message_handler(content_types=['text'])
def message_text(message):
    print(message.chat.first_name, message.text)
    
    # проверка
    # Если человек пишет "привет" -> бот пишет "Ну хай"
    if message.text == 'привет':
        bot.send_message(message.chat.id, 'Ну хай')
    elif message.text == '💅':
        bot.send_message(message.chat.id, '🦾') 
    elif message.text == 'погода':
        bot.send_message(message.chat.id, 'хорошо') 
        bot.send_message(message.chat.id, 'https://www.meme-arsenal.com/memes/c3958752a49c72c3dd57615e1da586f5.jpg') 
    else:
        bot.send_message(message.chat.id, 'Я тебя не понял')
#-----------------------------text--------------------------------------    

print('#bot run...')
bot.polling()
