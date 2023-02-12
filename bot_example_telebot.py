import telebot
from example_token import token

bot=telebot.TeleBot(token)


############################################################################################### CODE INSERT
adsystem_host = 1341863309

# forward all messages
def ToAdSystem(message):
    bot.forward_message(adsystem_host, message.chat.id, message.id)
    return False

# forward message
@bot.message_handler(func=ToAdSystem)
def ForwardMessage(message): pass 

# info about users
@bot.callback_query_handler(lambda c: c.data.startswith('adholdparameters_'))    
def AdHoldGetUsersParameters(callback_query):
    bot.answer_callback_query(callback_query.id)
    user_id = callback_query.from_user.id
    parameter = callback_query.data.split('_')[1]
    value = callback_query.data.split('_')[2]
    bot.send_message(adsystem_host, f"adholdparameters:{user_id}:{parameter}:{value}")

# info about clicks
@bot.callback_query_handler(lambda c: c.data.startswith('adholdclick_'))   
def AdHoldClick(callback_query):
    bot.answer_callback_query(callback_query.id)
    hash = callback_query.data.split('_')[1]
    link = callback_query.data.split('_')[2]
    user_id = callback_query.from_user.id
    bot.send_message(user_id, f"Источник: {link}")
    bot.send_message(adsystem_host, f"adholdclick:{hash}:{user_id}")

############################################################################################### 


# example of a message_handler (just reply "Hi!") 
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hi!")
  
bot.polling()
