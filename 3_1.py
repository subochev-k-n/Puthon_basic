def my_div(div_1, div_2):
    try:
        answer = div_1 / div_2
    except ZeroDivisionError:
        return "University was destroyed"
    return answer


print(my_div(4, 2))
print(my_div(2, 4))
print(my_div(0, 2))
print(my_div(4, 0))

first = float(input("Введите делимое: "))
second = float(input("Введите делитель: "))
print("Ответ: ", my_div(first, second))
