import argparse
import sys

from dotenv import load_dotenv
from src.scripts.settings import load_setting, save_setting
from src.scripts.tools import start_bot, start_bot_gui, start_bot_web

if __name__ == "__main__":
    load_dotenv()

    parser = argparse.ArgumentParser(prog="mika")

    parser.add_argument("--no-gui", action="store_true", help="Запуск без GUI")
    parser.add_argument("--gui", action="store_true", help="Запуск GUI")
    parser.add_argument("--web", action="store_true", help="Запуск в веб-режиме")
    parser.add_argument(
        "--set-default",
        choices=["gui", "no-gui", "web"],
        help="Установить значение по умолчанию для интерфейса"
    )

    args = parser.parse_args()

    if args.set_default:
        save_setting(args.set_default, "mode")
        print(f"Настройки по умолчанию изменены на: {args.set_default}")
        exit(0)

    setting = load_setting()

    if args.no_gui:
        start_bot()
    elif args.web:
        start_bot_web()
    elif args.gui:
        start_bot_gui()
    elif setting["mode"] == "no-gui":
        start_bot()
    elif setting["mode"] == "web":
        start_bot_web()
    elif setting["mode"] == "gui":
        start_bot_gui()
    else:
        sys.exit(
            f"Неверное значение интерфейса по умолчанию: {setting}. "
            f"Для установки нового значения, используйте --set-default <значение>. "
            f"Доступные значения: gui, no-gui, web"
        )
