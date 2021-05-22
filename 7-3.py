class Cell():

    def __init__(self, count):
        self.count = int(count)

    def __add__(self, other):
        self.count += other.count
        return self

    def __sub__(self, other):
        if self.count > other.count:
            self.count -= other.count
        else:
            print("Невозможно выполнить операцию вычитания!")
        return self

    def __mul__(self, other):
        self.count *= other.count
        return self

    def __truediv__(self, other):
        self.count = self.count // other.count
        return self

    def __str__(self):
        return '*' * (self.count) + " - " + str(self.count)

    def make_order(self, row):
        res_str = ''
        for i in range(self.count // row):
            res_str += '*' * row + '\n'
        res_str += '*' * (self.count % row) + '\n'
        return res_str


cell = Cell(24)
cell_2 = Cell(5)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(9))
