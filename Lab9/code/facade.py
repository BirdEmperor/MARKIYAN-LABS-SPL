from Lab1.runner import main as lb1
from Lab2.runner import main as lb2
from Lab3.lab3 import generate_ascii_art as lb3
from Lab4.lab4 import generate_ascii_art as lb4
from Lab5.main import main as lb5
from unittest import main as run_tests
from Lab7.main import main as lb7
from Lab8.UI.user_interface import main as lab8


class RunnerFacade:
    def __init__(self):
        self.labs = {
            1: self.run_lab1,
            2: self.run_lab2,
            3: self.run_lab3,
            4: self.run_lab4,
            5: self.run_lab5,
            6: self.run_lab6,
            7: self.run_lab7,
            8: self.run_lab8,
        }

    def show_menu(self):
        print("\nДоступні лабораторні роботи:")
        for lab_number in sorted(self.labs.keys()):
            print(f"{lab_number}: Лабораторна робота {lab_number}")
        print("0: Вихід")

    def run_lab(self, choice):
        if choice in self.labs:
            print(f"Запуск лабораторної {choice}...")
            self.labs[choice]()
        elif choice == 0:
            print("Вихід із програми.")
        else:
            print("Невірний вибір. Спробуйте ще раз.")

    def run_lab1(self):
        lb1()

    def run_lab2(self):
        lb2()

    def run_lab3(self):
        lb3()

    def run_lab4(self):
        lb4()

    def run_lab5(self):
        lb5()

    def run_lab6(self):
        run_tests(module="Lab6.test_calculator", exit=False)


    def run_lab7(self):
        lb7()

    def run_lab8(self):
        lab8()
