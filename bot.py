from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8298914165:AAENrUJyHcHL1Pg_RopEgQmCBoTj5excp_Y"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["بیمه شخص ثالث"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "سلام 👋\nلطفاً نوع بیمه مورد نظر را انتخاب کنید:",
        reply_markup=reply_markup
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
