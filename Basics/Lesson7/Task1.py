# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        text = ""
        for row in range(len(self.matrix)):
            for column in range(len(self.matrix[row])):
                text = f"{text}  {self.matrix[row][column]}"
            text = f"{text}\n"
        return text

    def __add__(self, other):
        matrixcolumn = []
        for row in range(len(self.matrix)):
            matrixrow = []
            for column in range(len(self.matrix[row])):
                matrixrow.append(self.matrix[row][column] + other.matrix[row][column])
            matrixcolumn.append(matrixrow)
        return Matrix(matrixcolumn)


matrix_1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix_2 = [[1,1,1],[2,2,2],[3,3,3]]

m1 = Matrix(matrix_1)
print(m1)

m2 = Matrix(matrix_2)
m3 = m1+m2
print(m3)
