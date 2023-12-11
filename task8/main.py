from itertools import combinations

def generate_subsets(input_set):
    all_subsets = []
    # Цикл пройде від 0 до n, визначаючи розмір підмножини
    for r in range(len(input_set) + 1):
        # Використовуємо combinations для отримання всіх комбінацій розміром r
        subsets_of_size_r = combinations(input_set, r)
        # Додаємо отримані підмножини до списку всіх підмножин
        all_subsets.extend(subsets_of_size_r)
    return all_subsets

# Вхідна множина
input_set = {1, 2, 3}
subsets = generate_subsets(input_set)

# Виводимо кожну підмножину на екран
for subset in subsets:
    print(set(subset))