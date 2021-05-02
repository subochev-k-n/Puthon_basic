time_in_sec = int(input("Введите время в секундах: "))
hours = time_in_sec // 3600
minutes = (time_in_sec - hours * 3600) // 60
seconds = time_in_sec % 60

print("Ваше время %02d:%02d:%02d" % (hours, minutes, seconds))
