def int_func(text):
    if text.isalpha():
        return text.title()
    else:
        return ''


numstr = input("Введите строку с пробелам между слов: ").split()

bigstr = ""
for n in numstr:
    if int_func(n) != '':
        bigstr = bigstr + " " + int_func(n)

print(bigstr)
