from colorama import Fore
from colorama import Fore, init
from Lab5.Shapes.shape3d import Shape3D


init(autoreset=True)  # Ініціалізація colorama для скидання кольорів після використання

class Shape3D:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def draw_2d(self):
        raise NotImplementedError("Цей метод має бути реалізований у підкласах.")

class Pyramid(Shape3D):
    def __init__(self, base_length, height, color, symbol='*'):
        super().__init__(color)
        self.base_length = base_length
        self.height = height
        self.symbol = symbol

    def draw_2d(self):
        color_code = getattr(Fore, self.color.upper(), Fore.RESET)
        lines = []

        for i in range(self.height):
            spaces_front = ' ' * (self.height - i - 1)
            depth_effect = '.' * i
            num_symbols = 2 * i + 1
            line_content = f"{spaces_front}{depth_effect}{self.symbol * num_symbols}{depth_effect}"
            lines.append(line_content)
            print(f"{color_code}{line_content}")

        return lines

    def save_to_file(self, filename="pyramid_output.txt"):
        lines = self.draw_2d()
        with open(filename, 'w', encoding='utf-8') as file:
            for line in lines:
                file.write(line + '\n')
        print(f"ASCII-арт успішно збережений у файл '{filename}'")

    def scale(self, factor):
        self.base_length = int(self.base_length * factor)
        self.height = int(self.height * factor)

    def translate(self, dx, dy):
        print(f"Зміщення піраміди на {dx} вправо і {dy} вниз.")

