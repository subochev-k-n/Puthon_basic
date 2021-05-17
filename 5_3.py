my_keys = dict()
with open("text_3.txt") as file3:
    for line in file3:
        temp = line.split()
        my_keys[temp[0]] = float(temp[1])

for m in my_keys:
    if my_keys[m] < 20000.0:
        print(m)
average_salary = sum(my_keys.values()) / len(my_keys.values())

print(average_salary)
