import json
import os

BOT_NAME = "Mika"
APP_NAME = f"Chatbot AI - {BOT_NAME}"

OUTPUT_DIR = "output"
SRC_PATH = "src"

MODEL_PATH = os.path.join(OUTPUT_DIR, "chatbot_model.h5")
WORDS_PATH = os.path.join(OUTPUT_DIR, "words.pkl")
CLASSES_PATH = os.path.join(OUTPUT_DIR, "classes.pkl")
LABEL_ENCODER_PATH = os.path.join(OUTPUT_DIR, "label_encoder.pkl")

JSONS_PATH = os.path.join(SRC_PATH, "jsons")
INTENTS_PATH = os.path.join(JSONS_PATH, "intents.json")

DEFAULT_SETTINGS_FILE = os.path.join(JSONS_PATH, "settings.json")

WORDS = []
CLASSES = []
DOCUMENTS = []

INTENTS = json.load(open(INTENTS_PATH, "r", encoding="utf-8"))
MODEL_EPOCHS = 300

BACKGROUND_COLOR = "black"
TEXT_COLOR = "white"
FONT_SIZE = "14px"
PADDING = "10px"
BORDER_COLOR = "#aaa"
BORDER_RADIUS = "5px"

SCROLLBAR_BACKGROUND = "#2b2b2b"
SCROLLBAR_HANDLE = "#808080"
SCROLLBAR_WIDTH = "10px"

SEND_BUTTON_BACKGROUND = "#0078d7"
SEND_BUTTON_PADDING = "10px"

INPUT_FIELD_BORDER_COLOR = "#ddd"
INPUT_FIELD_PADDING = "8px"
