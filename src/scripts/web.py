import threading
import webbrowser

from src.web.app import app


def open_chatbot_web():
    """
    Opens the chatbot web interface in a browser.

    This function starts the Flask web server for the chatbot web interface
    and opens the web interface in a browser. The web interface is available
    at http://127.0.0.1:5000.
    """

    threading.Timer(1, lambda: webbrowser.open("http://127.0.0.1:5000")).start()
    app.run(debug=False)
