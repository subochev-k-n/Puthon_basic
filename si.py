num = int(input("Введите целое положительное число: "))
max_found = 0

while num > 0:
    number = num % 10
    if number > max_found:
        max_found = number
    if max_found == 9:
        break
    num = num // 10

print(" Максимальное число: %d" % max_found)
