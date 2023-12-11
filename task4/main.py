def is_valid_identifier(s):
    # Перевірка, чи стрічка не містить пробіли
    if ' ' in s:
        return False

    # Перевірка, чи стрічка не містить цифр
    has_digit = False
    for char in s:
        if char.isdigit():
            has_digit = True
            break
    if has_digit:
        return False

    # Перевірка, чи стрічка складається лише з літер та нижнього підкреслення
    for char in s:
        if not (char.isalpha() or char == '_'):
            return False

    # Перевірка, чи стрічка не містить лише нижній або верхній регістр літер
    if s.islower() or s.isupper():
        return False

    # Якщо всі перевірки успішні, повертаємо True
    return True

# Перевірка для правильного ідентифікатора
identifier_1 = "my_variable"
result_1 = is_valid_identifier(identifier_1)
print(f"Is '{identifier_1}' a valid identifier? {result_1}")

# Перевірка для ідентифікатора із цифрою
identifier_2 = "var123"
result_2 = is_valid_identifier(identifier_2)
print(f"Is '{identifier_2}' a valid identifier? {result_2}")

# Перевірка для ідентифікатора із пробілами
identifier_3 = "invalid identifier"
result_3 = is_valid_identifier(identifier_3)
print(f"Is '{identifier_3}' a valid identifier? {result_3}")

# Перевірка для ідентифікатора із символом, що не є літерою чи нижнім підкресленням
identifier_4 = "my-variable"
result_4 = is_valid_identifier(identifier_4)
print(f"Is '{identifier_4}' a valid identifier? {result_4}")

# Перевірка для ідентифікатора із великими та малими літерами
identifier_5 = "MixedCase"
result_5 = is_valid_identifier(identifier_5)
print(f"Is '{identifier_5}' a valid identifier? {result_5}")