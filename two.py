ls = []
s = input("Введите эелементы списка: (для завершеения ввода введите 'nnn')")
while s != "nnn":
    ls.append(s)
    s = input()

print(ls)

for i in range(len(ls) // 2):
    temp = ls[i * 2]
    ls[i * 2] = ls[i * 2 + 1]
    ls[i * 2 + 1] = temp

print(ls)
