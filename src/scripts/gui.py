import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QTextBrowser, QPushButton

from src.scripts.chatbot import ChatBot
from src.scripts.config import *


class ChatBotInterface(QWidget):
    def __init__(self, chatbot):
        """
        Initializes the ChatBotInterface class by setting up the main window of the chatbot interface.

        Parameters:
        chatbot (ChatBot): The chatbot instance to use for generating responses.
        """

        super().__init__()

        self.chatbot = chatbot

        self.setWindowTitle(APP_NAME)
        self.setGeometry(100, 100, 400, 500)

        layout = QVBoxLayout()

        self.chat_display = QTextBrowser(self)
        self.chat_display.setStyleSheet(f"""
            background-color: {BACKGROUND_COLOR};
            color: {TEXT_COLOR};
            font-size: {FONT_SIZE};
            padding: {PADDING};
            border: 1px solid {BORDER_COLOR};
            border-radius: {BORDER_RADIUS};
                QScrollBar:vertical {{
                background: {SCROLLBAR_BACKGROUND};
                width: {SCROLLBAR_WIDTH};
                border-radius: {BORDER_RADIUS};
            }}
            
            QScrollBar::handle:vertical {{
                background: {SCROLLBAR_HANDLE};
                border-radius: {BORDER_RADIUS};
            }}
            
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
                background: none;
            }}
            
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {{
                background: none;
            }}
        """)

        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Введите ваше сообщение...")
        self.input_field.setStyleSheet(f"""
            padding: {INPUT_FIELD_PADDING};
            font-size: {FONT_SIZE};
            border: 1px solid {INPUT_FIELD_BORDER_COLOR};
        """)
        self.input_field.returnPressed.connect(self.handle_user_input)

        self.send_button = QPushButton("Отправить")
        self.send_button.setStyleSheet(f"""
            background-color: {SEND_BUTTON_BACKGROUND};
            color: {TEXT_COLOR};
            padding: {SEND_BUTTON_PADDING};
            font-size: {FONT_SIZE};
            border: none;
        """)
        self.send_button.clicked.connect(self.handle_user_input)

        layout.addWidget(self.chat_display)
        layout.addWidget(self.input_field)
        layout.addWidget(self.send_button)

        self.setLayout(layout)

    def handle_user_input(self):
        """
        Handles user input by sending it to the chatbot to generate a response.

        This method is called when the user presses the Enter key or the Send button.
        It retrieves the text from the input field, sends it to the chatbot to generate a response,
        and appends both the user's input and the chatbot's response to the chat display.
        The input field is then cleared.
        """

        user_text = self.input_field.text().strip()

        if user_text:
            self.chat_display.append(f"<b>Вы:</b> {user_text}")

            bot_response = self.chatbot.respond(user_text)

            self.chat_display.append(f"<b>Бот:</b> {bot_response}")
            self.input_field.clear()


def show_chatbot_interface(chatbot: ChatBot):
    """
    Launches the chatbot interface.

    Parameters:
    chatbot (ChatBot): The chatbot to be used in the interface.
    """

    print("Запуск приложения чат-бота.")

    app = QApplication(sys.argv)
    window = ChatBotInterface(chatbot)
    window.show()
    sys.exit(app.exec())
