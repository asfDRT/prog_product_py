"""
Этот модуль реализует простое приложение с графическим интерфейсом для вычисления корней с помощью tkinter.

Он включает в себя переводы на разные языки и поддержку открытия выпусков GitHub.
"""

import tkinter as tk
from tkinter import ttk, Menu
import webbrowser

from calculate import on_calculate

# Словарь для перевода
translations = {
    'en': {
        'value': "Value:",
        'degree_of_root': "Degree of Root:",
        'precision': "Precision:",
        'calculate': "Calculate",
        'result': "Result: ",
        'support': "Support",
        'github_support': "GitHub Support"
    },
    'ru': {
        'value': "Значение:",
        'degree_of_root': "Степень корня:",
        'precision': "Точность:",
        'calculate': "Вычислить",
        'result': "Результат: ",
        'support': "Поддержка",
        'github_support': "Поддержка GitHub"
    },
    'es': {
        'value': "Valor:",
        'degree_of_root': "Grado de Raíz:",
        'precision': "Precisión:",
        'calculate': "Calcular",
        'result': "Resultado: ",
        'support': "Soporte",
        'github_support': "Soporte GitHub"
    }
}

# Функция для обновления текстов виджетов
def update_language(lang):
    """
    Обновление языка элементов пользовательского интерфейса на основе выбранного языка.

    Parameters:
    lang (str): код выбранного языка («en», «ru», «es»).
    """
    value_label.config(text=translations[lang]['value'])
    degree_label.config(text=translations[lang]['degree_of_root'])
    precision_label.config(text=translations[lang]['precision'])
    calculate_button.config(text=translations[lang]['calculate'])
    result_label.config(text=translations[lang]['result'])
    # Обновляем названия в меню
    support_menu.entryconfig(0, label=translations[lang]['github_support'])


def open_github():
    """
    Открывает новую вкладку браузера, чтобы создать заявку GitHub для поддержки.
    """
    webbrowser.open_new("https://github.com/asfDRT/prog_product_py/issues/new")

# Основное окно приложения
root = tk.Tk()
root.title("Python Sqrt")
root.geometry("300x200")  # Фиксированный размер окна
root.resizable(False, False)


# Устанавливаем стандартные значения для полей ввода
default_value = tk.StringVar(value='')
default_degree = tk.StringVar(value='2')
default_precision = tk.StringVar(value='10')

# Меню сверху для языка
menu_bar = Menu(root)
root.config(menu=menu_bar)

language_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Language", menu=language_menu)

# Добавляем выбор языка в меню
language_menu.add_command(label="English", command=lambda: update_language('en'))
language_menu.add_command(label="Русский", command=lambda: update_language('ru'))
language_menu.add_command(label="Español", command=lambda: update_language('es'))

# Меню поддержки
support_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label=translations['en']['support'], menu=support_menu)
support_menu.add_command(label="GitHub", command=open_github)

# Создаем виджеты
value_label = ttk.Label(root, text="Value:")
value_label.pack()
value_entry = ttk.Entry(root, textvariable=default_value)
value_entry.pack()

degree_label = ttk.Label(root, text="Degree of Root:")
degree_label.pack()
degree_entry = ttk.Entry(root, textvariable=default_degree)
degree_entry.pack()

precision_label = ttk.Label(root, text="Precision:")
precision_label.pack()
precision_entry = ttk.Entry(root, textvariable=default_precision)
precision_entry.pack()

calculate_button = ttk.Button(root, text="Calculate", command=on_calculate)
calculate_button.pack()

result_label = ttk.Label(root, text="Result: ")
result_label.pack()

root.mainloop()


