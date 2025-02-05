import json
import os

from src.scripts.config import SETTINGS_FILE


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
