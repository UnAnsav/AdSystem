import adsystem           # import lib
i_am_ = "@__________"     # YOUR username 
dp.register_message_handler(adsystem.AdSystemConnectBot, adsystem.IAmTheOwner(i_am_, bot))      # New handlers for correct operation
dp.register_message_handler(adsystem.AdSystemMessage, adsystem.MessageToAdSystem())
dp.register_callback_query_handler(adsystem.AdSystemCallback, adsystem.CallbackToAdSystem())
dp.register_callback_query_handler(adsystem.AdSystemGetInterests, adsystem.AdSystemBot(False))
dp.register_message_handler(adsystem.AdSystemCaptcha, adsystem.AdSystemBot(True))
dp.register_message_handler(adsystem.AdSystemPhoto, adsystem.IsFromAdSystem(), content_types=['photo', 'text'])
