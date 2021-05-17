number_dict = {"Zero": "Ноль", "One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре",
               "Five": "Пять", "Six": "Шесть", "Seven": "Семь", "Eight": "Восемь", "Nine": "Девять"}
temp = []
i = 0
with open("text_4.txt") as file4:
    for line in file4:
        for key in number_dict:
            if line.find(key) >= 0:
                temp.append(str(line.replace(key, number_dict[key])))
                i += 1

with open("text_4_rus.txt", 'w') as file4r:
    file4r.writelines(temp)
