import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def histogram_by_price(data, ax):
    if 'Range(km)' in data.columns and 'Price(USD)' in data.columns:
        bins = [0, 20000, 40000, 60000, 80000, 100000, 150000]
        labels = ['<20k', '20k-40k', '40k-60k', '60k-80k', '80k-100k', '>100k']
        data['Price_Category'] = pd.cut(data['Price(USD)'], bins=bins, labels=labels)
        
        sns.histplot(data=data, x='Range(km)', hue='Price_Category', multiple='stack', palette='coolwarm', bins=15, ax=ax)
        ax.set_title('Розподіл діапазону пробігу за категоріями ціни')
        ax.set_xlabel('Діапазон пробігу (км)')
        ax.set_ylabel('Частота')

def scatter_plot(data, ax):
    if 'Range(km)' in data.columns and 'Price(USD)' in data.columns:
        sns.scatterplot(data=data, x='Range(km)', y='Price(USD)', hue='Model', palette='tab20', s=100, ax=ax)
        ax.set_title('Залежність ціни від діапазону пробігу')
        ax.set_xlabel('Діапазон пробігу (км)')
        ax.set_ylabel('Ціна (USD)')

def grouped_bar_chart(data, ax):
    if 'Model' in data.columns and 'Range(km)' in data.columns and 'Price(USD)' in data.columns:
        data_melted = data.melt(id_vars=['Model'], value_vars=['Range(km)', 'Price(USD)'], 
                                var_name='Characteristic', value_name='Value')
        
        sns.barplot(data=data_melted, x='Model', y='Value', hue='Characteristic', palette='Set2', ax=ax)
        ax.set_title('Груповані стовпчики для діапазону пробігу та ціни по моделях')
        ax.set_xlabel('Модель')
        ax.set_ylabel('Значення')
        ax.tick_params(axis='x', rotation=45)

def show_all_plots(data):
    fig, axs = plt.subplots(1, 4, figsize=(24, 6))
    
    histogram_by_price(data, axs[0])
    scatter_plot(data, axs[1])
    grouped_bar_chart(data, axs[2])
    
    sns.histplot(data=data, x='Price(USD)', kde=True, ax=axs[3], color='green')
    axs[3].set_title('Розподіл цін')
    axs[3].set_xlabel('Ціна (USD)')
    axs[3].set_ylabel('Частота')

    plt.tight_layout()
    plt.show()

def export_plots_as_image(data, format='png'):
    fig, axs = plt.subplots(1, 4, figsize=(24, 6))
    
    histogram_by_price(data, axs[0])
    scatter_plot(data, axs[1])
    grouped_bar_chart(data, axs[2])
    
    sns.histplot(data=data, x='Price(USD)', kde=True, ax=axs[3], color='green')
    axs[3].set_title('Розподіл цін')
    axs[3].set_xlabel('Ціна (USD)')
    axs[3].set_ylabel('Частота')
    
    plt.tight_layout()
    
    file_name = f"exported_plots.{format}"
    plt.savefig(file_name, format=format)
    print(f"Діаграми успішно експортовані в {file_name}")
    plt.close(fig)

def export_interactive_plot(data):
    fig = px.scatter(data, x='Range(km)', y='Price(USD)', color='Model',
                     title="Залежність ціни від діапазону пробігу", 
                     labels={'Range(km)': 'Діапазон пробігу (км)', 'Price(USD)': 'Ціна (USD)'})
    
    file_name = "interactive_plot.html"
    fig.write_html(file_name)
    print(f"Інтерактивна діаграма успішно експортована в {file_name}")
