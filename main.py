from src.scripts.chatbot import ChatBot

if __name__ == "__main__":
    chatbot = ChatBot()

    while True:
        user_input = input("Вы: ")
        print(chatbot.respond(user_input))
