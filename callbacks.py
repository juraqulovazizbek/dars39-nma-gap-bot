from telegram import (
    Update, 
    ReplyKeyboardMarkup, 
    KeyboardButton, 
    WebAppInfo, 
    InlineKeyboardMarkup, 
    InlineKeyboardButton,
)
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text=f'Assalomu alaykum {update.message.from_user.first_name}!',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(
                        text='🛍 Buyurtma berish',
                        web_app=WebAppInfo(url='https://uzum.uz')
                    )
                ],
                [
                    KeyboardButton(
                        text='📦 Buyurtmalarim'
                    ),
                    KeyboardButton(
                        text='⚙️ Sozlamalar'
                    )
                ],
                [
                    KeyboardButton(
                        text='ℹ️ Biz haqimizda'
                    ), 
                    KeyboardButton(
                        text='✍️ Fikr qoldirish'
                    )
                ]
            ],
            resize_keyboard=True,
        )
    )
    
def send_orders(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Sizda hali birorta ham buyurtma yo`q')
def sendFeedback(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Buyurtma berish uchun asosiy menyudagi “Buyurtma” tugmasidan foydalaning.\n\n"
        "Biz sizning fikr-mulohazalaringizni juda qadrlaymiz! "
        "Buyurtma berganingizdan so'ng, o'z fikr va mulohazalaringizni shu yerda qoldirishingiz mumkin."
    )
    
def send_about(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('shu yerda joylashganmiz')
    update.message.reply_markdown_v2('*Elektron pochta*: ||abror4work@gmail\.com||')
    
def send_settings(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text='⚙️ Sozlamalar',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(
                       text=("🌐 Tilni o'zgartirish")
                    )
                ],
                [
                    KeyboardButton(
                        text="📞 Telefon raqamingizni o'zgartiring"
                    )
                ],
                [
                    KeyboardButton(
                        text='Orqaga'
                    )
                ],
            ]
        )
    )
    
def change_language(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
         text="🌐 Tilni o'zgartirish",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(
                        text="🇺🇿 O'zbekcha"
                    )
                ],
                [
                    KeyboardButton(
                        text='🇷🇺 Русский'
                    )
                ],
                [
                    KeyboardButton(
                        text='🇺🇸 English'
                    )
                ],
                [
                    KeyboardButton(
                        text='Orqaga'
                    )
                ],
            ]
        )
    )
    
def change_phone_number(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text="📞 Iltimos, telefon raqamingizni yuboring",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(
                        text="📲 Mening telefon raqamim ",
                        request_contact=True
                    )
                ],
                [
                    KeyboardButton(
                        text="Orqaga"
                    )
                ]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
