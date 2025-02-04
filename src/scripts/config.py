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
