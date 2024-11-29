import pyfiglet
from colorama import Fore, Style, init
import os

# Ініціалізація colorama
init()

def preview_ascii_art(ascii_art, alignment):
    """Відображає попередній перегляд ASCII-арту з вибраним вирівнюванням."""
    terminal_width = os.get_terminal_size().columns
    print("\nПопередній перегляд вашого ASCII-арту:\n")
    
    # Центруємо попередній перегляд
    if alignment == "ліво":
        formatted_preview = "\n".join(line.ljust(terminal_width) for line in ascii_art.splitlines())
    elif alignment == "право":
        formatted_preview = "\n".join(line.rjust(terminal_width) for line in ascii_art.splitlines())
    else:
        formatted_preview = "\n".join(line.center(terminal_width) for line in ascii_art.splitlines())
    
    print(formatted_preview)
    print("\n--- Кінець попереднього перегляду ---\n")

def generate_ascii_art():
    # Завдання 1: Введення користувача
    text = input("Введіть слово або фразу для ASCII-арту: ")
    
    # Завдання 2: Набір символів
    symbol_set = input("Введіть символи для ASCII-арту (наприклад, '@#*'): ") or "*"

    # Завдання 3: Розміри Art-у
    while True:
        try:
            width = int(input("Введіть ширину ASCII-арту (рекомендовано більше 10): "))
            height = int(input("Введіть висоту ASCII-арту (рекомендовано більше 1): "))
            if width > 10 and height > 1:
                break
            else:
                print("Ширина повинна бути більше 10, а висота більше 1.")
        except ValueError:
            print("Будь ласка, введіть числове значення.")

    # Завдання 4: Функція генерації Art-у
    font = "standard"
    try:
        ascii_art = pyfiglet.figlet_format(text, font=font, width=width)
    except pyfiglet.FontNotFound:
        ascii_art = pyfiglet.figlet_format(text, font="standard", width=width)

    # Повторюємо кожен рядок для досягнення бажаної висоти
    art_lines = ascii_art.splitlines()
    scaled_art = "\n".join(line for line in art_lines for _ in range(height))

    # Завдання 5: Вирівнювання тексту
    alignment = input("Виберіть вирівнювання (ліво, центр, право): ").lower()
    alignment = alignment if alignment in ["ліво", "центр", "право"] else "центр"

    # Завдання 8: Варіанти кольорів
    print("Доступні кольори:")
    print("1. Червоний")
    print("2. Зелений")
    print("3. Синій")
    print("4. Стандартний (без кольору)")

    color_index = input("Введіть номер кольору для тексту: ")
    color = {
        '1': Fore.RED,
        '2': Fore.GREEN,
        '3': Fore.BLUE,
    }.get(color_index, Style.RESET_ALL)

    # Завдання 6: Відображення мистецтва
    print("\nВивід ASCII-арту з вибраними параметрами:\n")
    preview_ascii_art(scaled_art, alignment)

    # Завдання 9: Попередній перегляд
    preview = input("Чи хочете побачити попередній перегляд ASCII-арту? (так/ні): ").strip().lower()
    if preview in ['так', 'yes']:
        preview_ascii_art(scaled_art, alignment)

    # Завдання 7: Збереження у файл
    save_option = input("Чи хочете зберегти ASCII-арт у файл? (так/ні): ").strip().lower()
    if save_option in ['так', 'yes']:
        filename = input("Введіть ім'я файлу (без розширення, наприклад, 'ascii_art'): ") + '.txt'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(scaled_art)
        print(f"ASCII-арт збережено у файл: {filename}")

# Викликаємо функцію
generate_ascii_art()
