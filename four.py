user_str = input("Введите строку из нескольких слов: ")

my_list = user_str.split()
print(my_list)
for ind, enum in enumerate(my_list):
    print(ind, enum[0:10]) if len(enum) > 10 else print(ind, enum)
