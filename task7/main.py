def check_letters_present(input_string, word):
    # Переводимо слово та вхідну стрічку до множини букв
    word_set = set(word.lower())
    input_set = set(input_string.lower())

    # Перевіряємо, чи множина букв слова є підмножиною множини букв у стрічці
    return word_set.issubset(input_set)

# Приклад використання
input_string = "Hello, World!"
word_to_check = "world"
result = check_letters_present(input_string, word_to_check)
print(result)