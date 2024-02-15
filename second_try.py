def calculate_root_complex(value, degree=2, precision=10):
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


print(calculate_root_complex(14+2j, 2))