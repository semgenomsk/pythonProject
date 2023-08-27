"""
Создайте класс Матрица. Добавьте методы для:
- вывода на печать,
- сравнения,
- сложения,
- умножения матриц
"""

class Matrix:
    """Matrix -class матриц"""

    def __init__(self, matrix):
        """Проверим, что матрица задана правильно (все строки имеют одинаковую длину)"""
        if len(set(len(row) for row in matrix)) != 1:
            raise ValueError("Все строки матрицы должны иметь одинаковую длину")

        self.matrix = matrix

    def __str__(self):
        """Метод преобразуем матрицу в строку для вывода"""
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def __eq__(self, other):
        """Метод возвращает истину, если каждый элемент одной матрицы равен соответствующему элементу другой матрицы"""

        return self.matrix == other.matrix

    def __add__(self, other):
        """Метод сложения матриц возвращает – матрицу, все элементы которой представляют собой сложенные попарно
         соответствующие элементы исходных матриц"""
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Для сложения размеры матриц должны совпадать")

        res = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ]
        return Matrix(res)

    def __mul__(self, other):
        """Метод производит умножение матриц по правилу: произведением двух матриц А и В называется матрица С,
        элемент которой, находящийся на пересечении i-й строки и j-го столбца, равен сумме произведений элементов i-й
        строки матрицы А на соответствующие (по порядку) элементы j-го столбца матрицы В."""
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы")

        res = [
            [
                sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0])))
                for j in range(len(other.matrix[0]))
            ]
            for i in range(len(self.matrix))
        ]
        return Matrix(res)

if __name__ == '__main__':
    m1 = Matrix([[22, 2], [1, 7]])
    m2 = Matrix([[1, 3], [9, 5]])

    print(m1)
    print()
    print(m2)
    print()

    print(m1 + m2)
    print()

    print(m1 * m2)
    print()

    print(m1 == m2)