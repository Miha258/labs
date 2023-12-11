def find_trace(matrix):
    matrix_sum = 0
    for i in range(len(matrix)):
        matrix_sum += int(matrix[i][i])
    return matrix_sum

def find_min(a, b):
    return a if a < b else b

def read_matrix_from_file(matrix_file_path):
    with open(matrix_file_path, 'r') as f:
        lines = f.readlines()
        matrix = [line.strip().split(' ') for line in lines]
        return matrix

def write_matrix(matrix):
    with open('result.txt', 'w') as f:
        for line in matrix:
            f.write(" ".join(line) + "\n")
            
    
# Зчитування матриць з файлів
matrix_A = read_matrix_from_file('matrix_A.txt')
matrix_B = read_matrix_from_file('matrix_B.txt')
matrix_C = read_matrix_from_file('matrix_C.txt')

# Знаходження сліду та мінімуму для кожної матриці
trace_A = find_trace(matrix_A)
trace_B = find_trace(matrix_B)
trace_C = find_trace(matrix_C)

min_trace = find_min(trace_A, find_min(trace_B, trace_C))

# Знаходження матриці з мінімальним слідом
if min_trace == trace_A:
    result_matrix = matrix_A
elif min_trace == trace_B:
    result_matrix = matrix_B
else:
    result_matrix = matrix_C

# Записуєм результат у файл
write_matrix(result_matrix)