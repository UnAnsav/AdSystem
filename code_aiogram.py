from aiogram.contrib.fsm_storage.memory import MemoryStorage
import adsystemaiogram as adsystem      # import official library

storage = MemoryStorage()       # Temporary data storage
bot = Bot(TOKEN)                # Bot
dp = Dispatcher(bot, storage=storage)

i_am_ = "@yourusername"     # YOUR username 
# New handlers for correct operation
dp.register_message_handler(adsystem.AdSystemConnectBot, adsystem.IAmTheOwner(i_am_))
dp.register_message_handler(adsystem.AdSystemMessage, adsystem.MessageToAdSystem(bot))
dp.register_callback_query_handler(adsystem.AdSystemCallback, adsystem.CallbackToAdSystem(bot), state="*")
dp.register_callback_query_handler(adsystem.AdSystemGetInterests, adsystem.SaveBot(bot), state=adsystem.UserAnswers.interests_keyboard)
dp.register_message_handler(adsystem.AdSystemCaptcha, adsystem.SaveBot(bot), state=adsystem.UserAnswers.captcha, )
dp.register_message_handler(adsystem.AdSystemPhoto, adsystem.SaveBot(bot), adsystem.IsFromAdSystem(), content_types=['photo', 'text'])
