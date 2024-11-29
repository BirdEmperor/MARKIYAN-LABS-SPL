import sys
from Lab5.Shapes.pyramid import Pyramid

def main():
    print("Генератор 3D ASCII-арту: Піраміда")
    base_length = int(input("Введіть розмір основи піраміди (число): "))
    height = int(input("Введіть висоту піраміди (число): "))
    color = input("Введіть колір фігури (red, green, blue, yellow, magenta, cyan, white): ").strip().lower()
    symbol = input("Введіть символ для піраміди (наприклад, '*', '#', '@'): ")

    pyramid = Pyramid(base_length, height, color, symbol)
    pyramid.draw_2d()

    save_choice = input("Бажаєте зберегти піраміду у файл? (так/ні): ").strip().lower()
    if save_choice == 'так':
        filename = input("Введіть ім'я файлу для збереження (наприклад, output.txt): ")
        pyramid.save_to_file(filename)

    print("\nДякуємо за використання нашого генератора 3D ASCII-арту!")

if __name__ == "__main__":
    main()
