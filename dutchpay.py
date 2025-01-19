from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Replace with your bot's token
BOT_TOKEN = "7841693198:AAGbqaPCogZpDHc5yVuGH2FHNAsC3gg1FoI"

# Command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! I'm your Telegram bot. Type /help to see what I can do.")

# Command: /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Here are the commands you can use:\n"
                                    "/start - Start the bot\n"
                                    "/help - Show this help message\n"
                                    "Type anything else and I'll echo it back!")

# Echo handler (replies with the same message)
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

def main():
    # Create the Application and pass your bot's token
    application = Application.builder().token(BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Add a message handler for echoing text
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the script is stopped
    application.run_polling()

if __name__ == "__main__":
    main()
