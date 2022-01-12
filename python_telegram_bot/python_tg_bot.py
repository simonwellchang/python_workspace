from random import randint
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton


def start(update: Update, context: CallbackContext) -> None:
    a, b = randint(1, 100), randint(1, 100)
    update.message.reply_text(
        "{} + {} = ?".format(a, b),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        str(s), callback_data="{} {} {}".format(a, b, s)
                    )
                    for s in range(a + b - randint(1, 3), a + b + randint(1, 3))
                ]
            ]
        ),
    )


def answer(update: Update, context: CallbackContext) -> None:
    a, b, s = [int(x) for x in update.callback_query.data.split()]
    if a + b == s:
        update.callback_query.edit_message_text("你答對了！")
    else:
        update.callback_query.edit_message_text("你答錯囉！")


updater = Updater("5040646654:AAH_oyJ1TL7bx04po6QSwTqMgwHDgX3bkRI")

updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CallbackQueryHandler(answer))

updater.start_polling()
updater.idle()
