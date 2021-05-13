from functools import reduce

my_list = [el for el in range(100, 1001, 2)]

list_f = reduce(lambda a, b: a * b, my_list)
print(my_list)
print(list_f)
