import os
from telegram.ext import ApplicationBuilder



TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") 

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    print("salom")
    app.run_polling()
