import json
import os

from src.scripts.chatbot import ChatBot
from src.scripts.config import DEFAULT_SETTINGS_FILE
from src.scripts.gui import show_chatbot_interface


def load_setting():
    """
    Loads the default interface setting from a settings file.

    Checks if the settings file exists and reads the default interface setting from it.
    If the file does not exist or the default setting is not found, returns "gui".

    Returns:
    str: The default interface setting, either "gui", "no-gui", or "web".
    """

    if os.path.exists(DEFAULT_SETTINGS_FILE):
        with open(DEFAULT_SETTINGS_FILE, "r") as file:
            settings = json.load(file)
            return settings.get("mode")

    return "gui"


def save_setting(setting: str, arg: str):
    """
    Saves the default interface setting to a settings file.

    Checks if the settings file exists and reads it. Then updates the default
    interface setting with the given setting and writes back to the file.
    If the file does not exist, it will be created.

    Parameters:
    setting (str): The default interface setting, either "gui", "no-gui", or "web".
    """

    settings = {}

    if os.path.exists(DEFAULT_SETTINGS_FILE):
        with open(DEFAULT_SETTINGS_FILE, "r") as file:
            settings = json.load(file)

    settings[arg] = setting

    with open(DEFAULT_SETTINGS_FILE, "w") as file:
        json.dump(settings, file, indent=4)


def start_bot_web():
    """
    Starts the chatbot in web mode.

    This function initializes the chatbot and shows the chatbot web-interface.
    """

    print("Запуск чат-бота в веб-режиме.")


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
