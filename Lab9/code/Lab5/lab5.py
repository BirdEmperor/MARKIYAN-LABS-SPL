from colorama import Fore, init
import tkinter as tk

init()

# Основной класс для фигуры
class ASCIIArt3DShape:
    def __init__(self, size=5, color='white'):
        self.size = size
        self.color = color
        self.shape_data = []  # для хранения данных фигуры

    @staticmethod
    def get_user_input():
        shape_type = input("Введите тип фигуры (например, 'куб'): ")
        size = int(input("Введите размер фигуры: "))
        color = input("Выберите цвет (например, 'green'): ")
        return shape_type, size, color

    def scale(self, factor):
        # Изменяем размер куба
        new_size = max(1, int(self.size * factor))  # Минимальный размер — 1, чтобы избежать нуля
        self.size = new_size
        self.shape_data = [[' ']*self.size for _ in range(self.size)]
        self.draw()  # Перерисовываем куб с новым размером


    def shift(self, x_shift, y_shift):
        # Смещаем фигуру по x и y
        shifted_data = [[' ']*self.size for _ in range(self.size)]
        for i in range(len(self.shape_data)):
            for j in range(len(self.shape_data[i])):
                if 0 <= i + y_shift < self.size and 0 <= j + x_shift < self.size:
                    shifted_data[i + y_shift][j + x_shift] = self.shape_data[i][j]
        self.shape_data = shifted_data

    def save_to_file(self, filename="art_output.txt"):
        with open(filename, 'w', encoding='utf-8') as file:
            for line in self.project_to_2d():
                file.write(line + '\n')
        print(f"ASCII art saved to {filename}")

# Класс для куба
class Cube(ASCIIArt3DShape):
    def __init__(self, size=5, color='white'):
        super().__init__(size, color)
        self.shape_data = [[' ']*size for _ in range(size)]

    def draw(self):
    # Обозначаем границы куба в ASCII-символах
        for i in range(self.size):
            # Верхняя и нижняя границы
            self.shape_data[0][i] = '#'
            self.shape_data[self.size - 1][i] = '#'
            # Левая и правая границы
            self.shape_data[i][0] = '#'
            self.shape_data[i][self.size - 1] = '#'
    
        # Диагонали для создания объемного эффекта
        for i in range(1, self.size - 1):
            self.shape_data[i][i] = '#'
            if self.size - i - 1 > 0:
                self.shape_data[i][self.size - i - 1] = '#'


    def project_to_2d(self):
        # Проекция — добавляем символы по строкам
        projection = []
        for row in self.shape_data:
            projection.append(' '.join(row))
        return projection

    def display_ascii_art(self):
        color_map = {
            'red': Fore.RED,
            'green': Fore.GREEN,
            'blue': Fore.BLUE,
            'white': Fore.WHITE,
        }
        for line in self.project_to_2d():
            print(color_map.get(self.color, Fore.WHITE) + line + Fore.RESET)

# Класс для GUI интерфейса
class ArtApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ASCII Art Generator")
        self.label = tk.Label(self.root, text="ASCII Art 3D Generator")
        self.label.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.button = tk.Button(self.root, text="Generate", command=self.generate_art)
        self.button.pack()

    def generate_art(self):
        cube = Cube(size=5, color='blue')
        cube.draw()
        art = "\n".join(cube.project_to_2d())
        label = tk.Label(self.root, text=art, font=("Courier", 8))
        label.pack()

    def run(self):
        self.root.mainloop()

# Функция main для запуска программы
def main():
    print("Добро пожаловать в ASCII Art 3D Generator!")

    # Пример создания фигуры куба
    cube = Cube(size=25, color='blue')
    cube.draw()  # Построение куба
    print("\nПроекция 3D-куба в ASCII-арт:")
    cube.display_ascii_art()

    # Пример сохранения в файл
    save = input("Сохранить ASCII арт в файл? (yes/no): ")
    if save.lower() in ['yes', 'y']:
        filename = input("Введите имя файла (например, 'cube_art.txt'): ")
        cube.save_to_file(filename)

    # Пример манипуляции
    print("\nМанипуляция фигурой:")
    cube.scale(1.5)
    print("Увеличенный куб:")
    cube.display_ascii_art()

    # Смещение фигуры
    cube.shift(2, 2)
    print("Смещенный куб:")
    cube.display_ascii_art()

if __name__ == "__main__":
    main()
    # Для запуска GUI интерфейса, расскомментируйте строку ниже:
    app = ArtApp()
    app.run()
