"""принимает действительное положительное число x и целое отрицательное число y."""


def my_func_1(x, y):
    if x <= 0 or y >= 0:
        return "Out of range"
    return 1 / (x ** abs(y))


"""принимает действительное положительное число x и целое отрицательное число y."""


def my_func_2(x, y):
    if x <= 0 or y >= 0:
        return "Out of range"
    answer = x
    for i in range(1, abs(y)):
        answer *= x
    return 1 / answer


print(my_func_1(8, -2))

print(my_func_2(8, -2))
