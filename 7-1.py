class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result_str = ""
        max_len = 0
        for s in self.matrix:
            if len(s) > max_len:
                max_len = len(s)
        for s in self.matrix:
            for c in s:
                result_str += str(c) + "\t" if str(c).isdigit() else "0\t"
            for i in range(0, max_len - len(s)):
                result_str += "0\t"
            result_str = result_str[:-1]
            result_str += "\n"
        return result_str

    def __add__(self, matrix1):
        for i in range(len(self.matrix)):
            for j in range(len(matrix1.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] + matrix1.matrix[i][j]
        return self


m1 = Matrix([[1, 3, 1], [1, 6, 23], [2, 0, 1]])
m2 = Matrix([[1, 3, 1], [1, 6, 23], [2, 0, 1]])

print(m1)
print(m1 + m2)
