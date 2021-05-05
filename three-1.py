seasons = {"весна": [3, 4, 5], "лето": [6, 7, 8], "осень": [9, 10, 11], "зима": [12, 1, 2]}

month = int(input("Введите номер месяца: "))

for s in seasons.keys():

    if month in seasons.get(s):
        print(s)
        break

