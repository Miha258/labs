def count_diagonal_elements(matrix):
    diagonal_count = {}
    
    # Підрахунок елементів на головній діагоналі
    for i in range(len(matrix)):
        element = matrix[i][i]   
        # Якщо елемент не знайдений в diagonal_count, то 0 по замовчуванню
        diagonal_count[element] = diagonal_count.get(element, 0) + 1
    
    # Підрахунок елементів на бічній діагоналі
    for i in range(len(matrix)):
        element = matrix[i][len(matrix) - 1 - i]
        diagonal_count[element] = diagonal_count.get(element, 0) + 1
    
    return diagonal_count

# Приклад використання:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = count_diagonal_elements(matrix)
print(result)