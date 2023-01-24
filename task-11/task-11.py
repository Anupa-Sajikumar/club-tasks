import telebot
import random
bot_token = '5797937881:AAGerc-7xNZc-puL6mKAKGANDzoDhmIik1s'
bot = telebot.TeleBot(bot_token)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the stone-Paper-Scissors game! Please type /play to start a game.")
@bot.message_handler(commands=['play'])
def play_game(message):
    bot.reply_to(message, "Please type stone, paper, or scissors.")
    bot.register_next_step_handler(message, process_choice)
def process_choice(message):
    user_choice = message.text.lower()
    options = ["stone", "paper", "scissors"]
    if user_choice in options:
        bot_choice = random.choice(options)
        result = determine_winner(user_choice, bot_choice)
        bot.reply_to(message, f"You chose {user_choice} and the bot chose {bot_choice}. {result}")
    else:
        bot.reply_to(message, "Invalid choice. Please type stone, paper, or scissors.")
        bot.register_next_step_handler(message, process_choice)
def determine_winner(user_choice, bot_choice):
    if user_choice == bot_choice:
        return "It's a tie!"
    elif (user_choice == "stone" and bot_choice == "scissors") or (user_choice == "scissors" and bot_choice == "paper") or (user_choice == "paper" and bot_choice == "stone"):
        return "You win!"
    else:
        return "You lose!"
bot.polling()