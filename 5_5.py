num_str = ""
for n in range(1, 234, 16):
    num_str += str(n) + ' '
print(num_str)

with open("text_5.txt", 'w+') as file5:
    file5.write(num_str)
    file5.seek(0)
    file_sum = 0
    for s in file5.readline().split():
        file_sum += int(s)
    print(file_sum)
