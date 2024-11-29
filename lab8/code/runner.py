from ui import show_menu
from data_loader import load_data
from plots import histogram_by_price, scatter_plot, grouped_bar_chart, show_all_plots, export_plots_as_image, export_interactive_plot

def main():
    file_path = '/Users/markstas/Documents/ev_data.csv'  
    data = load_data(file_path)
    
    show_menu(data)

if __name__ == "__main__":
    main()


#/Users/markstas/labb8/runner.py
