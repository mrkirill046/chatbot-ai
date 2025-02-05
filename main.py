import argparse
import sys

from src.scripts.tools import load_setting, save_setting, start_bot, start_bot_gui, start_bot_web

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

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

    default_setting = load_setting()

    if args.no_gui:
        start_bot()
    elif args.web:
        start_bot_web()
    elif args.gui:
        start_bot_gui()

    if default_setting == "no-gui":
        start_bot()
    elif default_setting == "web":
        start_bot_web()
    elif default_setting == "gui":
        start_bot_gui()
    else:
        sys.exit(
            f"Неверное значение интерфейса по умолчанию: {default_setting}. "
            f"Для установки нового значения, используйте --set-default <значение>. "
            f"Доступные значения: gui, no-gui, web"
        )
