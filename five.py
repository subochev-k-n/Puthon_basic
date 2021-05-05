my_list = [7, 5, 3, 3, 2]
print(my_list)
user_e = int(input("Введите новый элемент рейтинга (1-9): "))

i = len(my_list)

while i > 0:
    if my_list[i - 1] >= user_e:
        my_list.insert(i, user_e)
        break
    else:
        i -= 1
if i == 0:
    my_list.insert(0, user_e)
print(my_list)
