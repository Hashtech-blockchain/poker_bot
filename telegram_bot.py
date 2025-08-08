from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Inserisci qui il token del tuo bot Telegram
TOKEN = "7685323526:AAFE2Bv1RYRq6SVtOvgsHVQMP_bo1I5QBsQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ciao! Benvenuto nel Poker Bot.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()