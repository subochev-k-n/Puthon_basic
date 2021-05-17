def num_clear(str):
    num_list = []
    num = ''
    for char in str:
        if char.isdigit():
            num += char
    if num == '':
        return int(0)
    return int(num)


my_keys = dict()
with open("text_6.txt") as file3:
    for line in file3:
        temp = line.split()
        #       print(temp)
        #        print(num_clear(temp[1]) + num_clear(temp[2]) + num_clear(temp[3]))
        my_keys[temp[0].replace(':', '')] = num_clear(temp[1]) + num_clear(temp[2]) + num_clear(temp[3])

print(my_keys)
