from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
import os
from argos import generate_response
import time
from datetime import datetime
from pytz import timezone

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

application = Application.builder().token(TELEGRAM_TOKEN).build()

active_sessions = {}
dm_sessions = {}

def log_interaction(user):
    log_entry = [
        (user.first_name or "N/A") + " " + (user.last_name or "N/A"),
        user.username or "N/A",
        user.id,
        datetime.now(timezone('Asia/Kolkata')).strftime("%d-%b-%Y %I:%M %p")
    ]
    print(log_entry)

    with open("argos_logs.txt", "a", encoding="utf-8") as log_file:
        log_file.write(str(log_entry) + "\n")

async def start_debate(update: Update, context):
    chat_id = update.message.chat_id
    if chat_id in active_sessions:
        await update.message.reply_text("A debate session is already active in this chat!")
    else:
        active_sessions[chat_id] = True
        await update.message.reply_text("Debate session started! Type your arguments, and I'll respond. Use /stop to end the session.")
        log_interaction(update.message.from_user)

async def stop_debate(update: Update, context):
    chat_id = update.message.chat_id
    if chat_id in active_sessions:
        del active_sessions[chat_id]
        await update.message.reply_text("Debate session ended. Thank you for debating with Argos!")
    elif update.message.from_user.id in dm_sessions:
        del dm_sessions[update.message.from_user.id]
        await update.message.reply_text("Debate session ended. Thank you for debating with Argos!")
    else:
        await update.message.reply_text("No active debate session in this chat.")

async def restart_debate(update: Update, context):
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id

    if chat_id in active_sessions:
        del active_sessions[chat_id]
        await update.message.reply_text("Debate session ended. Starting a new debate...")
        active_sessions[chat_id] = True
        await update.message.reply_text("New debate session started! Type your arguments, and I'll respond. Use /stop to end the session.")
    elif user_id in dm_sessions:
        del dm_sessions[user_id]
        await update.message.reply_text("Debate session ended. Starting a new debate in DM...")
        dm_sessions[user_id] = True
        await update.message.reply_text("New debate session started in DM! Type your arguments, and I'll respond. Use /stop to end the session.")
    else:
        await update.message.reply_text("No active debate session to restart. Use /start to begin a new debate.")

async def dm_debate(update: Update, context):
    user_id = update.message.from_user.id
    if user_id in dm_sessions:
        await update.message.reply_text("You already have an active debate session in DM!")
    else:
        dm_sessions[user_id] = True
        await update.message.reply_text("Debate session started in DM! Type your arguments, and I'll respond. Use /stop to end the session.")

async def handle_message(update: Update, context):
    user_id = update.message.from_user.id
    chat_id = update.message.chat_id

    if chat_id in active_sessions or user_id in dm_sessions:
        try:
            response = generate_response(update.message.text)
            await update.message.reply_text(response)
        except Exception as e:
            await update.message.reply_text("Sorry, I couldn't process your request. Please try again later.")
            print(f"Error: {e}")

application.add_handler(CommandHandler("start", start_debate))
application.add_handler(CommandHandler("stop", stop_debate))
application.add_handler(CommandHandler("restart", restart_debate))  # Add restart handler
application.add_handler(CommandHandler("dm", dm_debate))

application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

if __name__ == "__main__":
    while True:
        try:
            print("Starting the bot...")
            print("bot started")
            application.run_polling()
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Restarting the bot in 1 second...")
            time.sleep(1)
