# Telegram-athkar-bot
Hi guys 
if you're facing this problem while you try to create your Telegram Bots.
problem:
  @my_bot.message_handler(content_types="text")
AttributeError: 'TeleBot' object has no attribute 'message_handler'   
Try this solution:
1- open the terminal on your text editor.
2- past this command : 
pip3 uninstall telebot
pip3 uninstall PyTelegramBotAPI
pip3 install pyTelegramBotAPI
pip3 install --upgrade pyTelegramBotAPI
