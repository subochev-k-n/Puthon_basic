first_day_km = float(input("Введите километраж в первый день: "))
max_limit = float(input("Введите минимальный порог общего результата: "))
day = 1
while first_day_km < max_limit:
    first_day_km *= 1.1
    day += 1
print(day)
