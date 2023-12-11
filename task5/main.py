def remove_digit_words(sentence):
    # Розділити речення на слова
    words = sentence.split()
    # Зберегти тільки ті слова, які не складаються з цифр
    filtered_words = [word for word in words if not word.isdigit()]
    # З'єднати залишені слова у відфільтроване речення
    return ' '.join(filtered_words)


def process_file():
    input_file_path = 'input.txt'
    output_file_path = 'output.txt'
    # Зчитати всі рядки з вхідного файлу
    with open(input_file_path, 'r', encoding = 'utf-8') as f:
        lines = f.readlines()
    # Застосувати функцію remove_digit_words до кожного рядка
    modified_lines = [remove_digit_words(line) for line in lines]

    # Записати модифіковані рядки у вихідний файл
    with open(output_file_path, 'w', encoding = 'utf-8') as f:
        for modified_line in modified_lines:
            f.write(modified_line)

# Приклад використання
process_file()