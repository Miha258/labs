def check_all(arr):
    pass

def check_any(arr):
    for i in arr:
        if i == True:
            return True

def find_last_positive(arr):
    # Початкове число, якщо нічого не знайдено то поверне -1
    last_positive = -1
    # Перевертаєм список
    reversed_arr = arr[::-1]
    for num in reversed_arr:
        # Провіряєм чи число більше 0, якщо ні, то провіряєм далі
        if num > 0:
            last_positive = num
            break 
    return last_positive

# Масив довільних числ
numbers = [1, -2, 3, 0, -5, 7, -8]
# Отримуєм шукане число через функцію і зберігаєм результат у змінну
result = find_last_positive(numbers)
# Резултат: 7
print(result)