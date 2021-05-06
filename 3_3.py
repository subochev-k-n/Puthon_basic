def my_func(val_1, val_2, val_3):
    temp = min(val_1, val_2)
    if temp > val_3:
        return val_1 + val_2
    else:
        if temp == val_1:
            return val_2 + val_3
        else:
            return val_1 + val_3


print(my_func(1, 2, 3))
print(my_func(3, 2, 1))
print(my_func(2, 1, 3))
print(my_func(3, 1, 2))
print(my_func(2, 3, 1))
print(my_func(1, 3, 2))

print(my_func(1, 1, 3))
print(my_func(1, 3, 1))
print(my_func(3, 1, 1))

print(my_func(2, 3, 3))
print(my_func(3, 2, 3))
print(my_func(3, 3, 2))

print(my_func(3, 3, 3))
