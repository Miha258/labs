def find_students_by_grade(students_dict, target_grade):
    # Створюємо пустий список для зберігання імен студентів
    matching_students = []

    # Проходимо кожного студента в словнику
    for student, grades in students_dict.items():
        # Перевіряємо, чи має студент хоча б одну оцінку, рівну цільовій
        if any(grade == target_grade for grade in grades):
            matching_students.append(student)

    # Повертаємо список імен студентів з потрібною оцінкою
    return matching_students

def get_students():
    with open('students.txt', 'r', encoding = 'utf-8') as f:
        students = f.readlines()
        # Проходимо кожен рядок та розділяємо ім'я студента і його оцінки
        students_dict = {}
        for student in students:
            if student:
                parts = student.split(' - ')
                name = parts[0]
                grades_str = parts[1]
                grades = [int(grade) for grade in grades_str.split(', ')]
                students_dict[name] = grades
    return students_dict

# Визначте цільову оцінку
target_grade = 5

# Викликаємо функцію та отримуємо список студентів з цільовою оцінкою
result_students = find_students_by_grade(get_students(), target_grade)

# Виводимо результат на екран
print(result_students)