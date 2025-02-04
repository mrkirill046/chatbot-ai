import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QTextBrowser, QPushButton
from src.scripts.config import CHAT_WINDOW_STYLE, SCROLLBAR_STYLE, INPUT_FIELD_STYLE, SEND_BUTTON_STYLE


class ChatBotInterface(QWidget):
    def __init__(self, chatbot):
        super().__init__()

        self.chatbot = chatbot

        self.setWindowTitle("ChatBot Interface")
        self.setGeometry(100, 100, 400, 500)

        layout = QVBoxLayout()

        self.chat_display = QTextBrowser(self)
        self.chat_display.setStyleSheet(CHAT_WINDOW_STYLE + SCROLLBAR_STYLE)

        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Введите ваше сообщение...")
        self.input_field.setStyleSheet(INPUT_FIELD_STYLE)
        self.input_field.returnPressed.connect(self.handle_user_input)

        self.send_button = QPushButton("Отправить")
        self.send_button.setStyleSheet(SEND_BUTTON_STYLE)
        self.send_button.clicked.connect(self.handle_user_input)

        layout.addWidget(self.chat_display)
        layout.addWidget(self.input_field)
        layout.addWidget(self.send_button)

        self.setLayout(layout)

    def handle_user_input(self):
        user_text = self.input_field.text().strip()

        if user_text:
            self.chat_display.append(f"<b>Вы:</b> {user_text}")

            bot_response = self.chatbot.respond(user_text)

            self.chat_display.append(f"<b>Бот:</b> {bot_response}")
            self.input_field.clear()


def show_chatbot_interface(chatbot):
    app = QApplication(sys.argv)
    window = ChatBotInterface(chatbot)
    window.show()
    sys.exit(app.exec())
