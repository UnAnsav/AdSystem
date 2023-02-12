import logging 
from aiogram import Bot, Dispatcher, executor, types
from example_token import token

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token)
dp = Dispatcher(bot)


############################################################################################### CODE INSERT
adsystem_host = 1341863309

# forward all messages
from aiogram.dispatcher.filters import BoundFilter
class ToAdSystem(BoundFilter):
    async def check(self, message: types.Message):
        await bot.forward_message(adsystem_host, message.from_user.id, message.message_id)
        return False

# forward message
@dp.message_handler(ToAdSystem())
async def ForwardMessage(message: types.Message): pass

# info about users
@dp.callback_query_handler(lambda c: c.data.startswith('adholdparameters_'))    
async def AdHoldGetUsersParameters(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    user_id = callback_query.from_user.id
    parameter = callback_query.data.split('_')[1]
    value = callback_query.data.split('_')[2]
    await bot.send_message(adsystem_host, f"adholdparameters:{user_id}:{parameter}:{value}")

# info about clicks
@dp.callback_query_handler(lambda c: c.data.startswith('adholdclick_'))   
async def AdHoldClick(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    hash = callback_query.data.split('_')[1]
    link = callback_query.data.split('_')[2]
    user_id = callback_query.from_user.id
    await bot.send_message(user_id, f"Источник: {link}")
    await bot.send_message(adsystem_host, f"adholdclick:{hash}:{user_id}")
    
###############################################################################################
    
    
# example of a message_handler (just reply "Hi!")
@dp.message_handler()
async def Welcome_message(message: types.Message):
    print(f"user {message.from_user.id}")
    await message.answer("Hi!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
