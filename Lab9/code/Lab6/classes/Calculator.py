import math

class Calculator:
    def __init__(self, decimal_places=2):
        self.num1 = 0.0
        self.num2 = 0.0
        self.operator = ''
        self.result = None
        self.decimal_places = decimal_places
        self.memory = {}  # Словник для збереження результатів
        self.history = []  # Список для збереження історії обчислень

    def get_user_input(self):
        print("\n--- Введіть дані для обчислення ---")
        try:
            self.num1 = float(input("Введіть перше число: "))
            self.operator = input("Введіть оператор (+, -, *, /, %, ^, √): ").strip()
            if self.operator != '√':
                self.num2 = float(input("Введіть друге число: "))
            else:
                self.num2 = None  # Для оператора '√' друге число не потрібно
        except ValueError:
            print("Помилка: введено некоректне число. Спробуйте знову.")
            self.get_user_input()

    def check_operator(self):
        if self.operator not in ['+', '-', '*', '/', '%', '^', '√']:
            print("Невірний оператор! Доступні оператори: +, -, *, /, %, ^, √")
            return False
        return True

    def calculate(self):
        print("\n--- Виконання обчислення ---")
        if self.operator == '+':
            self.result = self.num1 + self.num2
        elif self.operator == '-':
            self.result = self.num1 - self.num2
        elif self.operator == '*':
            self.result = self.num1 * self.num2
        elif self.operator == '/':
            self.result = self.num1 / self.num2 if self.num2 != 0 else "Помилка: ділення на нуль!"
        elif self.operator == '%':
            self.result = self.num1 % self.num2 if self.num2 != 0 else "Помилка: ділення на нуль!"
        elif self.operator == '^':
            self.result = self.num1 ** self.num2
        elif self.operator == '√':
            self.result = math.sqrt(self.num1) if self.num1 >= 0 else "Помилка: корінь з від'ємного числа!"
        
        # Додаємо результат в історію
        self.history.append(f"{self.num1} {self.operator} {self.num2 if self.operator != '√' else ''} = {self.result}")

    def display_result(self):
        print("\n--- Результат ---")
        if isinstance(self.result, str):
            print(self.result)
        else:
            print(f"Результат обчислення: {self.result:.{self.decimal_places}f}")

    def repeat(self):
        while True:
            repeat = input("\nБажаєте виконати ще одне обчислення? (так/ні): ").lower().strip()
            if repeat == 'так':
                return True
            elif repeat == 'ні':
                print("\nДякуємо за використання калькулятора. До побачення!")
                return False
            else:
                print("Невірна відповідь. Будь ласка, введіть 'так' або 'ні'.")

    def save_to_memory(self, key):
        """Зберегти результат в пам'яті під вказаним ключем."""
        self.memory[key] = self.result  # Зберігаємо результат в пам'яті
        print(f"Результат збережено в пам'яті під ключем '{key}'.")

    def retrieve_from_memory(self, key):
        """Отримати результат з пам'яті за вказаним ключем."""
        return self.memory.get(key, "Ключ не знайдено в пам'яті.")