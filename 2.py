not_my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

my_list = [el for el, el2 in zip(not_my_list[1::], not_my_list[:-1:]) if el > el2]
print(my_list)


#