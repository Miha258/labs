def generate_subsets(input_set):
    # Створюємо пустий список для зберігання всіх підмножин
    all_subsets = []
    # Отримуємо кількість елементів у вхідній множині
    n = len(input_set)

    # Зовнішній цикл пройде 2^n разів, де n - кількість елементів
    for i in range(2**n):
        # Перетворюємо число i у його двійкове представлення
        subset = [input_set[j] for j in range(n) if (i // (2**j)) % 2 == 1]
        
        # Додаємо підмножину до списку всіх підмножин
        all_subsets.append(subset)
    
    # Повертаємо список всіх підмножин
    return all_subsets