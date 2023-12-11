def count_unique_numbers(matrix):
    # Створюємо пустий список для зберігання унікальних чисел
    unique_numbers = []
    # Проходимо кожен рядок у матриці
    for row in matrix:
        # Додаємо унікальні числа до списку
        unique_numbers.extend(set(row))
    # Використовуємо множину для отримання унікальних чисел
    unique_numbers_set = set(unique_numbers)
    # Повертаємо кількість унікальних чисел
    return len(unique_numbers_set)

# Викликаємо функцію та виводимо результат
matrix = [
    [1.2, 3.4, 2.1],
    [4.5, 1.2, 6.7],
    [3.4, 8.9, 1.2]
]
result = count_unique_numbers(matrix)
print(result)