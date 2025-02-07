from src.scripts.chatbot import ChatBot
from src.scripts.gui import show_chatbot_interface
from src.scripts.web import open_chatbot_web


def start_bot_web():
    """
    Starts the chatbot in web mode.

    This function initializes the chatbot and shows the chatbot web-interface.
    """

    print("Запуск чат-бота в веб-режиме.")
    open_chatbot_web()


def start_bot_gui():
    """
    Starts the chatbot in GUI mode.

    This function initializes the chatbot and shows the chatbot interface.
    """

    print("Запуск чат-бота в графическом интерфейсе.")
    chatbot = ChatBot()
    show_chatbot_interface(chatbot)


def start_bot():
    """
    Starts the chatbot in console mode.

    This function prints a greeting message and enters an infinite loop where it
    waits for user input. If the user enters an empty string, it asks for input again.
    If the user enters "exit", the loop is broken and the function returns. Otherwise,
    the chatbot's response is printed to the console.
    """

    print("Запуск чат-бота в консоли. Введите 'выход' для завершения.")
    chatbot = ChatBot()

    while True:
        user_input = input("Вы: ")

        if not user_input:
            print("Я вас не понимаю. Пожалуйста, повторите ввод.")
            continue

        if user_input.lower() == "выход":
            break

        bot_response = chatbot.respond(user_input)
        print(f"Бот: {bot_response}")
