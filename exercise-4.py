import telebot

TOKEN = '2104263688:AAGZPd27nqN5PN1OgS-XI7WSx88W3xe8vYw'


bot = telebot.TeleBot(TOKEN, parse_mode='html')

welcome_text = 'Здравствуйте!'



@bot.message_handler(content_types=['text'])
def auto_handler(message):
    text = message.text.lower()
    def search_chars(text):
        letters = ['a', 'i', 'e', 'u', 'y', 'o']
        count = 0
        for chars in text:
            if chars in letters:
                count +=1
        bot.send_message(message.from_user.id, f'Гласных слов в слове: {count}')
    search_chars(text)



bot.infinity_polling()





