class MyExcept(Exception):
    def __init__(self, txt):
        self.txt = txt


me_list = []
next_el = input("Для завершения нажмите 'stop', для ввода следующего элемента нажмите любую клавишу.")

while True:
    try:
        if next_el == 'stop':
            break
        else:
            if next_el.isdigit():
                me_list.append(next_el)
                next_el = input()
            else:
                raise MyExcept("Вы ввели не число! Повторите ввод числа")

    except MyExcept as err:
        print(err)
        next_el = input()
print(f"Ваш список = {me_list}")
