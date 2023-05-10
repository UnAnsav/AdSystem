import logging 
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

TOKEN = "123456789:EREhmvhu8wrvikuejdse"

# REPLACED CODE
''' 
bot = Bot(TOKEN)
dp = Dispatcher(bot)
'''

############################################################################################### REPLACE THE CODE WITH

from aiogram.contrib.fsm_storage.memory import MemoryStorage
import adsystemaiogram as adsystem

storage = MemoryStorage()       # Temporary data storage
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=storage)

i_am_ = "@yourusername"     # YOUR username 
dp.register_message_handler(adsystem.AdSystemConnectBot, adsystem.IAmTheOwner(i_am_))
dp.register_message_handler(adsystem.AdSystemMessage, adsystem.MessageToAdSystem(bot))
dp.register_callback_query_handler(adsystem.AdSystemCallback, adsystem.CallbackToAdSystem(bot), state="*")
dp.register_callback_query_handler(adsystem.AdSystemGetInterests, adsystem.SaveBot(bot), state=adsystem.UserAnswers.interests_keyboard)
dp.register_message_handler(adsystem.AdSystemCaptcha, adsystem.SaveBot(bot), state=adsystem.UserAnswers.captcha, )
dp.register_message_handler(adsystem.AdSystemPhoto, adsystem.SaveBot(bot), adsystem.IsFromAdSystem(), content_types=['photo', 'text'])

############################################################################################### END CODE 

    
@dp.message_handler()
async def Welcome_message(message: types.Message):
    name = message.from_user.first_name
    print(message)
    await message.reply(f"Hi, {name}! ")

    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)   
