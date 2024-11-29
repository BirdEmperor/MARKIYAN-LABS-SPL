from colorama import Fore, init

# Ініціалізація colorama
init(autoreset=True)


class Shape3D:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def draw_2d(self):
        raise NotImplementedError("Цей метод має бути реалізований у підкласах.")