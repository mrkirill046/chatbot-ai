import json
import os

OUTPUT_DIR = "output"
SRC_PATH = "src"

MODEL_PATH = os.path.join(OUTPUT_DIR, "chatbot_model.h5")
WORDS_PATH = os.path.join(OUTPUT_DIR, "words.pkl")
CLASSES_PATH = os.path.join(OUTPUT_DIR, "classes.pkl")
LABEL_ENCODER_PATH = os.path.join(OUTPUT_DIR, "label_encoder.pkl")

JSONS_PATH = os.path.join(SRC_PATH, "jsons")
INTENTS_PATH = os.path.join(JSONS_PATH, "intents.json")

WORDS = []
CLASSES = []
DOCUMENTS = []

INTENTS = json.load(open(INTENTS_PATH, "r", encoding="utf-8"))
MODEL_EPOCHS = 300

CHAT_WINDOW_STYLE = """
    background-color: black;
    color: white;
    font-size: 14px;
    padding: 10px;
    border: 1px solid #aaa;
    border-radius: 5px;
"""

SCROLLBAR_STYLE = """
    QScrollBar:vertical {
        background: #2b2b2b;
        width: 10px;
        border-radius: 5px;
    }
    QScrollBar::handle:vertical {
        background: #808080;
        border-radius: 5px;
    }
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        background: none;
    }
    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
        background: none;
    }
"""

INPUT_FIELD_STYLE = """
    padding: 8px;
    font-size: 14px;
    border: 1px solid #ddd;
"""

SEND_BUTTON_STYLE = """
    background-color: #0078d7;
    color: white;
    padding: 10px;
    font-size: 14px;
    border: none;
"""
