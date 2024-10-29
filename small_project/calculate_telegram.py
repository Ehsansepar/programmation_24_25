# import telebot

# # Remplacez 'YOUR_BOT_TOKEN' par le token de votre bot Telegram
# bot = telebot.TeleBot('7257160237:AAHe-rc9-OOpT7qUFezf-0siYYIwi5A0afs')

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, "Bienvenue ! Envoyez-moi une expression mathématique et je la calculerai pour toi.")

# @bot.message_handler(func=lambda message: True)
# def calculate_expression(message):
#     try:
#         # Calcul simple en une seule ligne
#         result = eval(message.text)
#         bot.reply_to(message, f"Résultat: {result}")
#     except Exception as e:
#         bot.reply_to(message, f"Erreur : {e}")

# bot.polling()


import telebot
from telebot import types
from sympy import symbols, Eq, solve

# Remplacez 'YOUR_BOT_TOKEN' par le token de votre bot Telegram
bot = telebot.TeleBot('7257160237:AAHe-rc9-OOpT7qUFezf-0siYYIwi5A0afs')

# Variables pour stocker les données temporaires de l'utilisateur
user_data = {}
x = symbols('x')  # Définition de la variable symbolique

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Bienvenue ! Choisissez une opération pour commencer.")
    
    # Créer un clavier avec des boutons pour les opérateurs et la résolution d'équations
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn_add = types.KeyboardButton('+')
    btn_subtract = types.KeyboardButton('-')
    btn_multiply = types.KeyboardButton('×')
    btn_divide = types.KeyboardButton('÷')
    btn_solve_equation = types.KeyboardButton('Résoudre une équation')
    markup.add(btn_add, btn_subtract, btn_multiply, btn_divide, btn_solve_equation)

    # Envoyer le clavier à l'utilisateur
    bot.send_message(message.chat.id, "Sélectionnez une opération :", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ['+', '-', '×', '÷'])
def ask_first_number(message):
    user_data[message.chat.id] = {'operation': message.text}
    bot.send_message(message.chat.id, "Entrez le premier nombre :")
    bot.register_next_step_handler(message, ask_second_number)

def ask_second_number(message):
    try:
        user_data[message.chat.id]['first_number'] = float(message.text)
        bot.send_message(message.chat.id, "Entrez le deuxième nombre :")
        bot.register_next_step_handler(message, calculate_result)
    except ValueError:
        bot.send_message(message.chat.id, "Veuillez entrer un nombre valide.")
        ask_first_number(message)

def calculate_result(message):
    try:
        user_data[message.chat.id]['second_number'] = float(message.text)
        first_num = user_data[message.chat.id]['first_number']
        second_num = user_data[message.chat.id]['second_number']
        operation = user_data[message.chat.id]['operation']

        # Effectuer le calcul en fonction de l'opération choisie
        if operation == '+':
            result = first_num + second_num
        elif operation == '-':
            result = first_num - second_num
        elif operation == '×':
            result = first_num * second_num
        elif operation == '÷':
            if second_num != 0:
                result = first_num / second_num
            else:
                bot.send_message(message.chat.id, "Erreur : Division par zéro.")
                return

        bot.send_message(message.chat.id, f"Résultat : {result}")
        send_welcome(message)
        
    except ValueError:
        bot.send_message(message.chat.id, "Veuillez entrer un nombre valide.")
        ask_second_number(message)

@bot.message_handler(func=lambda message: message.text == 'Résoudre une équation')
def ask_equation(message):
    bot.send_message(message.chat.id, "Entrez une équation avec 'x' (exemple : 2*x + 3 = 7) :")
    bot.register_next_step_handler(message, solve_equation)

def solve_equation(message):
    try:
        # Remplacer '=' par '==' pour que sympy puisse comprendre l'égalité
        equation_str = message.text.replace("=", "==")
        equation = Eq(eval(equation_str.split("==")[0]), eval(equation_str.split("==")[1]))
        
        # Résoudre l'équation
        solutions = solve(equation, x)
        bot.send_message(message.chat.id, f"Solution(s) pour x : {solutions}")
    except Exception as e:
        bot.send_message(message.chat.id, "Erreur dans l'équation. Assure toi de bien entrer une équation correcte.")
    send_welcome(message)

bot.polling()
