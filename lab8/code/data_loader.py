import pandas as pd

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print(f"Дані успішно завантажено з {file_path}")
        return data
    except Exception as e:
        print(f"Помилка при завантаженні даних: {e}")
        return pd.DataFrame()  # Повертаємо порожній DataFrame, якщо виникла помилка
