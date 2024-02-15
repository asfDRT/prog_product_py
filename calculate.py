from decimal import Decimal, getcontext
import cmath

"""
В этом модуле предусмотрены функции для вычисления корней, как сложных, так и вещественных.

Он включает в себя функции для вычисления корня комплексного числа и корня действительного числа с заданной точностью.
"""


def calculate_root_complex(value, degree=2):
    """
    Вычислить корень комплексного числа.

       Parameters:
           value (комплексное, строковое или плавающее): комплексное число.
           degree  (int): Степень корня (по умолчанию — 2).

       Returns:
           complex: вычисленный корень.

       """
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


def calculate_root(value, degree, precision):
    """
        Вычислить корень действительного числа с заданной точностью.

        Parameters:
            value (float or str): число.
            degree (int): степень корня.
            precision (int): точность вычисления.

        Returns:
            decimal.Decimal: вычсленный корень.

        """
    getcontext().prec = precision
    value = Decimal(value)
    if value >= 0:
        return value**(Decimal(1)/Decimal(degree))
    else:
        return cmath.exp(cmath.log(value)/degree)


def on_calculate():
    """
       Выполняет расчет на основе входных значений и обновление метку результата.

    """
    from UI import value_entry, degree_entry, precision_entry, result_label
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


