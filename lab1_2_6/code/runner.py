import sys
import os

from classes.Сalculator import Calculator

def main():
    print("Ласкаво просимо до калькулятора!\n")
    calc = Calculator()

    while True:
        calc.get_user_input()
        if calc.check_operator():
            calc.calculate()
            calc.display_result()

            # Запит на збереження результату в пам'яті
            save_memory = input("Бажаєте зберегти результат в пам'яті? (так/ні): ").lower().strip()
            if save_memory == 'так':
                key = input("Введіть ключ для збереження: ")
                calc.save_to_memory(key)  # Виклик методу збереження

            # Запит на перегляд історії
            view_history = input("Бажаєте переглянути історію обчислень? (так/ні): ").lower().strip()
            if view_history == 'так':
                print("\n--- Історія обчислень ---")
                for entry in calc.history:
                    print(entry)

            if not calc.repeat():
                break

if __name__ == "__main__":
    main()
