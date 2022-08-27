import telebot
import requests
my_bot = telebot.TeleBot("Token")

def replay(mes,str):
  my_bot.send_message(mes.from_user.id,str)

def send(mes,letter):
  for x in range(5):
    content = requests.get(f"https://azkar-api.nawafhq.repl.co/zekr?{letter}&json").json()
    my_bot.send_message(mes.from_user.id,content['content'])

@my_bot.message_handler(content_types="text")
def get_text_messages(message):
  if message.text in("/start","start/","ابدأ","ابدا"):
    my_bot.send_message(message.from_user.id,f"""
     في حال واجهتك اي مشكلة تواصل معي
      {"https://mobile.twitter.com/_ii404"}
        """)

    keyboard = telebot.types.InlineKeyboardMarkup()
    button_welc = telebot.types.InlineKeyboardButton(text='ادعية', callback_data='ادعية')
    keyboard.add(button_welc)
    button_welc = telebot.types.InlineKeyboardButton(text='اذكار', callback_data='اذكار')
    keyboard.add(button_welc)
    button_welc = telebot.types.InlineKeyboardButton(text='تسابيح و اذكار عشوائية', callback_data='تسابيح')
    keyboard.add(button_welc)
    my_bot.send_message(message.chat.id, f" اهلا {message.from_user.first_name} مرحبا بك في بوت الادعية والاذكار  \n الرجاء اختيار القسم", reply_markup=keyboard)
  else:

    my_bot.send_message(message.from_user.id,f"""
      عذرا لم افهمك.
   /start للبدء اضغط
   او اكتب كلمة ابدأ""")

@my_bot.callback_query_handler(func= lambda v:True)
def rep(mes):

  if (mes.data=="ادعية"):

    keyb = telebot.telebot.types.InlineKeyboardMarkup()

    option = telebot.telebot.types.InlineKeyboardButton(text= "ادعية قرانية",callback_data="قران")
    keyb.add(option)
    option = telebot.telebot.types.InlineKeyboardButton(text= "ادعية الانبياء",callback_data="الانبياء")
    keyb.add(option)

    my_bot.send_message(mes.from_user.id,"تم اختيار قسم الادعية",reply_markup=keyb)



  elif(mes.data=="اذكار"):
      keyb = telebot.types.InlineKeyboardMarkup()
      option = telebot.types.InlineKeyboardButton(text= "اذكار الصباح ",callback_data="الصباح")
      keyb.add(option)
      option = telebot.types.InlineKeyboardButton(text= "اذكار المساء",callback_data="المساء")
      keyb.add(option)
      option = telebot.types.InlineKeyboardButton(text= "اذكار قبل النوم",callback_data="النوم")
      keyb.add(option)
      option = telebot.types.InlineKeyboardButton(text= "أذكار بعد السلام من الصلاة المفروضة",callback_data="السلام")
      keyb.add(option)
      my_bot.send_message(mes.from_user.id,f"تم اختيار قسم الاذكار",reply_markup=keyb)
  elif(mes.data=="الصباح"):
     replay(mes,"تم اختيار اذكار الصباح")
     send(mes,"m")
  elif(mes.data=="المساء"):
    replay(mes,"تم اختيار اذكار المساء")
    send(mes,"e")
  elif(mes.data=="النوم"):
      replay(mes,"تم اختيار اذكار قبل النوم")
      send(mes,"bs")
  elif(mes.data=="السلام"):
      replay(mes,"تم اختيار أذكار بعد السلام من الصلاة المفروضة-")
      send(mes,"as")
  elif(mes.data=="تسابيح"):
      replay(mes,"تم اختيار تسابيح و اذكار عشوائية-")
      send(mes,"t")
  elif(mes.data=="قران"):
      replay(mes,"تم اختيار أدعية قرآنية")
      send(mes,"qd")
  elif(mes.data=="الانبياء"):
      replay(mes,"تم اختيار أدعية الأنبياء")
      send(mes,"pd")




my_bot.infinity_polling()