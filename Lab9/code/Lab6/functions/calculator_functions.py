import math

def perform_calculation(num1, operator, num2=None):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2 if num2 != 0 else "Помилка: ділення на нуль!"
    elif operator == '%':
        return num1 % num2 if num2 != 0 else "Помилка: ділення на нуль!"
    elif operator == '^':
        return num1 ** num2
    elif operator == '√':
        return math.sqrt(num1) if num1 >= 0 else "Помилка: корінь з від'ємного числа!"
    else:
        return "Невірний оператор!"
