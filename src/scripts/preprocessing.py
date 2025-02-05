import nltk
import pickle

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from src.scripts.config import INTENTS, WORDS_PATH, CLASSES_PATH

nltk.download("punkt")
nltk.download("stopwords")

lemmatizer = WordNetLemmatizer()


def clean_up_sentence(sentence: str):
    """
    Cleans up a given sentence by tokenizing it, lemmatizing its words and converting them to lower case.

    Parameters:
    sentence (str): The sentence to clean up.

    Returns:
    list: A list of lower case lemmatized words from the sentence.
    """

    sentence_words = nltk.word_tokenize(sentence)
    stop_words = set(stopwords.words("russian"))

    return [lemmatizer.lemmatize(w.lower()) for w in sentence_words if w.lower() not in stop_words]


def bow(sentence: str, words: list):
    """
    Creates a bag-of-words representation of a sentence based on a predefined list of words.

    Parameters:
    sentence (str): The input sentence to be converted into a bag-of-words.
    words (list): A list of words to use as the vocabulary for the bag-of-words.

    Returns:
    list: A list of 0s and 1s representing the presence or absence of each word in the input sentence.
    """

    sentence_words = clean_up_sentence(sentence)
    return [1 if w in sentence_words else 0 for w in words]


def preprocess_data():
    """
    Preprocesses the data for training a chatbot model. This involves

    1. Tokenizing all words from the patterns of the intents.
    2. Removing stopwords from the list of words.
    3. Lemmatizing all words.
    4. Removing duplicates from the list of words.
    5. Storing the words and classes in a file using pickle.

    Returns:
        tuple: A tuple of three elements: a list of words, a list of classes and a list of documents.
    """

    words, classes, documents = [], [], []

    for intent in INTENTS["intents"]:
        for pattern in intent["patterns"]:
            word_list = nltk.word_tokenize(pattern)
            words.extend(word_list)
            documents.append((pattern, intent["tag"]))

        if intent["tag"] not in classes:
            classes.append(intent["tag"])

    words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in nltk.corpus.stopwords.words("russian")]
    words = sorted(list(set(words)))
    classes = sorted(list(set(classes)))

    pickle.dump(words, open(WORDS_PATH, "wb"))
    pickle.dump(classes, open(CLASSES_PATH, "wb"))

    return words, classes, documents
