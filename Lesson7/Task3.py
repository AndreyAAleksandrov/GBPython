# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.


class Cell:
    
    def __init__(self, qty):
        self.qty = int(qty)

    def __add__(self, other):
        self.qty += other.qty
        return self.qty

    def __sub__(self, other):
        self.qty -= other.qty
        return self.qty

    def __truediv__(self, other):
        self.qty //= other.qty
        return self.qty

    def __mul__(self, other):
        self.qty *= other.qty
        return self.qty

    def __str__(self):
        return "(" + str(self.qty) +") " + "*"*self.qty

    def make_order(self, row):
        text = ''
        for i in range(int(self.qty / row)):
            text += '*' * row + '\n'
        text += '*' * (self.qty % row) + '\n'
        return text


cell_1 = Cell(18)
cell_2 = Cell(3)
print("Cell 1", cell_1)
print("Cell 2", cell_2)
cell_1 + cell_2
print("1 + 2", cell_1)
cell_1 - cell_2
print("1 - 2", cell_1)
cell_1 / cell_2
print("1 / 2", cell_1)
cell_1 * cell_2
print("1 * 2", cell_1)
print(cell_1.make_order(5))
