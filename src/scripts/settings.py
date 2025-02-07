import json
import os

from src.scripts.config import SETTINGS_FILE, USER_DATA_FILE


def load_setting():
    """
    Loads the default interface setting from a settings file.

    Checks if the settings file exists and reads the default interface setting from it.
    If the file does not exist or the default setting is not found, returns "gui".

    Returns:
    str: The default interface setting, either "gui", "no-gui", or "web".
    """

    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as file:
            return json.load(file)

    return None


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

    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as file:
            settings = json.load(file)

    settings[arg] = setting

    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file, indent=2)


def load_user_data():
    """
    Loads the user data from a file.

    Checks if the file exists and reads the user data from it.
    If the file does not exist, returns None.

    Returns:
    dict: The user data dictionary.
    """

    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)["data"]

    return None


def save_user_data(data: dict):
    """
    Saves the user data to a file.

    Checks if the directory of the file exists and creates it if not.
    Then writes the user data to the file.

    Parameters:
    data (dict): The user data dictionary.
    """

    if not os.path.exists(os.path.dirname(USER_DATA_FILE)):
        os.makedirs(os.path.dirname(USER_DATA_FILE), exist_ok=True)

    with open(USER_DATA_FILE, "w", encoding="utf-8") as file:
        json.dump({"data": data}, file, ensure_ascii=False, indent=2)
