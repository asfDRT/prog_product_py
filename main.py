import cmath
from decimal import Decimal, getcontext
import tkinter as tk
from tkinter import ttk


import cmath




def calculate_root_complex(value, degree=2):
    try:
        # Проверяем, является ли входное значение комплексным числом
        if isinstance(value, complex) or 'j' in str(value):
            value = complex(value)
        else:
            value = float(value)
        # Возвращаем корень из комплексного числа
        result = value ** (1 / degree)
        return result
    except Exception as e:
        return str(e)


def calculate_root(value, degree=2, precision=10):
    getcontext().prec = precision
    value = Decimal(value)
    if value >= 0:
        return value**(Decimal(1)/Decimal(degree))
    else:
        return cmath.exp(cmath.log(value)/degree)

def on_calculate():
    try:
        # Принимаем строку ввода как есть, без преобразования в float
        value_str = value_entry.get()
        # Проверяем, содержит ли строка 'j' для комплексных чисел
        if 'j' in value_str:
            value = complex(value_str)
            degree = int(degree_entry.get())
            precision = int(precision_entry.get())
            result = calculate_root_complex(value, degree)
            result_label.config(text=f"Result: {result}")
        else:
            value = float(value_str)
            degree = int(degree_entry.get())
            precision = int(precision_entry.get())
            result = calculate_root(value, degree, precision)
            result_label.config(text=f"Result: {result}")

    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")


root = tk.Tk()
root.title("Root Calculator")

value_label = ttk.Label(root, text="Value:")
value_label.pack()
value_entry = ttk.Entry(root)
value_entry.pack()

degree_label = ttk.Label(root, text="Degree of Root:")
degree_label.pack()
degree_entry = ttk.Entry(root)
degree_entry.pack()

precision_label = ttk.Label(root, text="Precision:")
precision_label.pack()
precision_entry = ttk.Entry(root)
precision_entry.pack()

calculate_button = ttk.Button(root, text="Calculate", command=on_calculate)
calculate_button.pack()

result_label = ttk.Label(root, text="Result: ")
result_label.pack()

root.mainloop()
