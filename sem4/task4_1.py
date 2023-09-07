"""
Напишите функцию для транспонирования матрицы
"""

matrix = [[9, 22, 13], [45, 25, 26], [67, 78, 99]]


def transpose_matrix(matrix):
    trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix


print(f"Исходная матрица:\n{matrix}")
print(f"Транспонированная матрица:\n{transpose_matrix(matrix)}")