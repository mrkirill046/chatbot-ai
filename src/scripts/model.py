import numpy as np
import pickle

from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.preprocessing import LabelEncoder
from src.scripts.config import *
from src.scripts.preprocessing import preprocess_data, bow


def create_model(input_size: int, output_size: int):
    """
    Creates a model with the specified input and output size.

    The model consists of a sequence of three layers: two dense layers with ReLU
    activation and dropout, and a final dense layer with softmax activation.

    Parameters:
    input_size (int): The size of the input layer.
    output_size (int): The size of the output layer.

    Returns:
    model (Sequential): The created model.
    """

    model = Sequential()
    model.add(Dense(265, input_shape=(input_size,), activation="relu"))
    model.add(Dropout(0.4))
    model.add(Dense(128, activation="relu"))
    model.add(Dropout(0.4))
    model.add(Dense(output_size, activation="softmax"))
    model.compile(
        loss="sparse_categorical_crossentropy",
        optimizer=Adam(learning_rate=0.001),
        metrics=["accuracy"]
    )

    return model


def load_or_train_model():
    """
    Loads a model, list of words, list of classes and a label encoder if all the necessary files exist.
    Otherwise, preprocesses the data, creates a model, trains it, saves the model and the data, and returns everything.

    Returns:
    model (Sequential): The loaded or trained model.
    words (list): The list of words.
    classes (list): The list of classes.
    label_encoder (LabelEncoder): The label encoder.
    """

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if all(os.path.exists(path) for path in [MODEL_PATH, WORDS_PATH, CLASSES_PATH, LABEL_ENCODER_PATH]):
        model = load_model(MODEL_PATH)
        words = pickle.load(open(WORDS_PATH, "rb"))
        classes = pickle.load(open(CLASSES_PATH, "rb"))
        label_encoder = pickle.load(open(LABEL_ENCODER_PATH, "rb"))
    else:
        words, classes, documents = preprocess_data()

        training_data = [bow(doc[0], words) for doc in documents]
        training_labels = [doc[1] for doc in documents]

        label_encoder = LabelEncoder()
        training_labels = label_encoder.fit_transform(training_labels)

        pickle.dump(label_encoder, open(LABEL_ENCODER_PATH, "wb"))

        model = create_model(len(words), len(classes))
        early_stopping = EarlyStopping(monitor="accuracy", patience=MODEL_PATIENCE, restore_best_weights=True)

        model.fit(
            np.array(training_data),
            np.array(training_labels),
            epochs=MODEL_EPOCHS, batch_size=5, verbose=1,
            callbacks=[early_stopping]
        )

        model.save(MODEL_PATH)
        pickle.dump(words, open(WORDS_PATH, "wb"))
        pickle.dump(classes, open(CLASSES_PATH, "wb"))

    return model, words, classes, label_encoder
