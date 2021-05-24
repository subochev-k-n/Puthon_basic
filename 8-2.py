class MyExcept(Exception):

    def __init__(self, txt):
        self.txt = txt


user_data = input("Введите делитель числа 100: ")

try:
    user_data = int(user_data)
    if user_data == 0:
        raise MyExcept("Вы ввели нулевое значение!")
except ValueError:
    print("Вы ввели не число")
except MyExcept as err:
    print(err)
else:
    print(f"Ура вселенная спасена 100/{user_data} = {100 / user_data}")
