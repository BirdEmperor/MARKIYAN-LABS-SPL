import matplotlib.pyplot as plt
from plots import histogram_by_price, scatter_plot, grouped_bar_chart, show_all_plots, export_plots_as_image, export_interactive_plot

def show_menu(data):
    print("Виберіть одну з опцій:")
    print("1. Показати гістограму діапазону пробігу за категоріями ціни")
    print("2. Показати scatter plot для ціни та діапазону пробігу")
    print("3. Показати груповану стовпчикову діаграму для діапазону пробігу та ціни")
    print("4. Показати всі діаграми разом")
    print("5. Експортувати всі діаграми як зображення (PNG/SVG)")
    print("6. Експортувати інтерактивну діаграму як HTML")
    
    choice = input("Введіть 1, 2, 3, 4, 5 або 6: ").strip()

    if choice == '1':
        histogram_by_price(data, plt.gca())  # Викликаємо для поточної осі
        plt.show()
    elif choice == '2':
        scatter_plot(data, plt.gca())  # Викликаємо для поточної осі
        plt.show()
    elif choice == '3':
        grouped_bar_chart(data, plt.gca())  # Викликаємо для поточної осі
        plt.show()
    elif choice == '4':
        show_all_plots(data)  # Показуємо всі діаграми
    elif choice == '5':
        format_choice = input("Виберіть формат для експорту (png/svg): ").strip().lower()
        export_plots_as_image(data, format=format_choice)  # Експортуємо як зображення
    elif choice == '6':
        export_interactive_plot(data)  # Експортуємо інтерактивну діаграму
    else:
        print("Невірний вибір. Будь ласка, виберіть 1, 2, 3, 4, 5 або 6.")
