from math import factorial


def fact(m):
    for fel in range(1, m):
        yield factorial(fel)


n = int(input("Введите число n: "))

i = 0
for el in fact(n):
    print(el)
