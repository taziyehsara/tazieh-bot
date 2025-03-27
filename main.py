from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7510867442:AAECdJD9XNWUqXg6Z4OhDAKWtI_PXWLhKwg"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ ربات فعال شد!")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()