import os
import asyncio
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Bot token will be stored in environment variable (safer for hosting)
BOT_TOKEN = os.getenv("8311101203:AAHA9sZBe0m3-c_tWrGOHFx3Ov4XebYLsN4")

# File name of your QR image
QR_IMAGE = "qr.png"

# Auto reply function
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # First message
    first_message = (
        "👋 Hello!\n\n"
        "To join the group, please pay **₹100** and send the payment screenshot.\n\n"
        "📲 Scan the QR code below to pay 👇"
    )

    # Send text message
    await update.message.reply_text(first_message, parse_mode="Markdown")

    # Send QR code image
    await update.message.reply_photo(photo=open(QR_IMAGE, "rb"))

    # Wait 5 seconds before sending verification message
    await asyncio.sleep(120)

    # Second message
    second_message = "⏳ After sending, please wait for verification ✅"
    await update.message.reply_text(second_message)

def main():
    # Build the bot application
    app = Application.builder().token(BOT_TOKEN).build()

    # Listen for any message in private chat
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    print("✅ Bot is running on Render/Local...")
    app.run_polling()

if __name__ == "__main__":
    main()
