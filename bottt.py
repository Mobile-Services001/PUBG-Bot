import telebot
from telebot import types

# Token အသစ်ကို ထည့်သွင်းထားပါတယ်
API_TOKEN = '8816488778:AAFt4PSGsc19pjX-Y5j6Gn-tMSkGfMPp8Dw'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # သင်ဝိုင်းပြထားတဲ့ ပုံစံအတိုင်း
    photo_url = "https://images.unsplash.com/photo-1542751371-adc38448a05e?q=80&w=600&auto=format&fit=crop"
    
    caption_text = (
        "⚡ *PUBG HACKING OBB* ⚡\n\n"
        "Welcome to the Ultimate Hacking Bot! 🔥\n\n"
        "လူကြီးမင်းတို့ လိုချင်တဲ့ Hacking Files များကို အောက်က ခလုတ်တွေမှာ ရွေးချယ်ဝယ်ယူနိုင်ပါပြီဗျာ။"
    )
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # ခလုတ် (၃) ခု
    btn_pubg = types.InlineKeyboardButton(text="🛒 PUBG Hacking File ဝယ်ရန်နှိပ်ပါ", url="https://t.me/pubghack_hacking_fileobb_shop")
    btn_mlbb = types.InlineKeyboardButton(text="🛒 MLBB Hacking File ဝယ်ရန်နှိပ်ပါ", url="https://t.me/mlbb_new_datafile_bot")
    btn_contact = types.InlineKeyboardButton(text="💬 သိချင်တာစုံစမ်းရန်နှိပ်ပါ", url="https://t.me/pubg_hacking_myanmar")
    
    markup.add(btn_pubg, btn_mlbb, btn_contact)
    
    bot.send_photo(message.chat.id, photo=photo_url, caption=caption_text, reply_markup=markup, parse_mode="Markdown")

print("🔥 MAIN BOT IS RUNNING SUCCESSFULLY... 🔥")
bot.infinity_polling()
