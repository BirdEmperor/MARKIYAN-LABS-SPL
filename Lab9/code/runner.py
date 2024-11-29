import sys
import os
from facade import RunnerFacade

current_dir = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(root_path)

def __main__():
    facade = RunnerFacade()
    while True:
        facade.show_menu()
        try:
            choice = int(input("Оберіть лабораторну роботу: "))
            if choice == 0:
                break
            facade.run_lab(choice)
        except ValueError:
            print("Введіть коректний номер лабораторної роботи.")

if __name__ == "__main__":
    __main__()
