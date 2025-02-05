import numpy as np
import random
import datetime

from src.scripts.preprocessing import bow
from src.scripts.config import INTENTS
from src.scripts.model import load_or_train_model


class ChatBot:
    def __init__(self):
        """
        Initializes the ChatBot class by loading or training the model,
        along with associated words, classes, and label encoder.
        """

        self.model, self.words, self.classes, self.label_encoder = load_or_train_model()

    def predict_class(self, sentence: str):
        """
        Predicts the class of the given sentence using the model.

        Parameters:
        sentence (str): The sentence to predict the class of.

        Returns:
        prediction (numpy.ndarray): A numpy array of shape (1, n_classes) containing the output of the model.
        """

        bow_input = np.array([bow(sentence, self.words)])
        prediction = self.model.predict(bow_input)

        return prediction

    def respond(self, sentence: str):
        """
        Generates a response for the given sentence by predicting its class and selecting a random response
        from the corresponding intent in the predefined intents.

        Parameters:
        sentence (str): The input sentence for which a response is to be generated.

        Returns:
        str: A response string based on the predicted intent of the input sentence.
        """

        predicted_class = self.predict_class(sentence)
        predicted_label = self.label_encoder.inverse_transform([np.argmax(predicted_class)])
        tag = predicted_label[0]

        for intent in INTENTS["intents"]:
            if intent["tag"] == tag:
                response = random.choice(intent["responses"])

                if tag == "time":
                    response = response.replace("{time}", datetime.datetime.now().strftime("%H:%M"))

                return response

        return "Извините, я не понимаю вас."
