import telebot, random
from bot_logic import gen_pass
from telebot.types import ReactionTypeEmoji


token = '8453865910:AAFZc2PIu_0vM9hilXfJRZV9sQOptRXvPcs'
bot = telebot.TeleBot(token)
    

@bot.message_handler(commands=['start', 'старт'])
def send_welcome(message):
    bot.reply_to(message, "привет, используй команду /каналы")

@bot.message_handler(commands=['каналы'])
def send_channels(message):
    bot.reply_to(message, 'твич:https://www.twitch.tv/luxays228')
    


@bot.message_handler(commands=['password'])
def send_password(message):
    bot.reply_to(message, gen_pass(10))

@bot.message_handler(func=lambda message: True)
def send_reaction(message):
    emo = ["\U0001F525", "\U0001F917", "\U0001F60E"]  # or use ["🔥", "🤗", "😎"]
    bot.set_message_reaction(message.chat.id, message.id, [ReactionTypeEmoji(random.choice(emo))], is_big=False)


bot.polling()
