print("Привет!")
name = input(" Как тебя зовут?")
f_n_ages = 48
age = int(input("Сколько тебе лет?" ))

if age > f_n_ages:
    print(name + "! Ричард Фенйман получил нобелевскую премию в 48 лет. А чего добился ты?")
else:
    print(name + "!Ричард Фенйман получил нобелевскую премию в 48 лет. Старайся, тебе осталось %d лет" % (f_n_ages - age))

