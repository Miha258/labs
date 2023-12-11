def find_last_positive_with_index(arr):
    # Змінні для зберігання останнього додатнього числа та його індексу
    last_positive = -1
    last_positive_index = -1
    for i in len(arr):
        # Перевірка, чи елемент є додатнім
        if arr[i] > 0:
            # Збереження останнього додатнього числа та його індексу
            last_positive = arr[i]
            last_positive_index = i
    
    # Повернення кортежу із знайденими значеннями
    return last_positive, last_positive_index

# Функція для заміни останнього додатнього числа на 1000
def replace_last_positive_with_1000(arr):
    # Виклик функції для знаходження останнього додатнього числа та його індексу
    last_positive, index = find_last_positive_with_index(arr)
    # Перевірка, чи було знайдено додатнє число
    if last_positive != -1:
        # Заміна останнього додатнього числа на 1000
        arr[index] = 1000


# Задання три масиви цілих чисел
array_A = [1, -2, 3, 0, -5, 7, -8]
array_B = [-4, -2, -6, -1, -3]
array_C = [0, -1, -2, -3, -4]

# Заміна останнього додатнього числа на 1000 у кожному масиві
replace_last_positive_with_1000(array_A)
replace_last_positive_with_1000(array_B)
replace_last_positive_with_1000(array_C)

# Вивід результатів
print("Масив A після заміни:", array_A) # [1, -2, 3, 0, -5, 1000, -8]
print("Масив B після заміни:", array_B) # [-4, -2, -6, -1, -3]
print("Масив C після заміни:", array_C) # [0, -1, -2, -3, -4]