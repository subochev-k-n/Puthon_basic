class Stationery():
    title = "Stationery"

    def draw(self):
        print("Запуск отрисовки.")


class Pencil(Stationery):
    title = "Pencil"

    def draw(self):
        print("Грифель хрустит.")


class Pen(Stationery):
    title = "Pen"

    def draw(self):
        print("Шарик крутится.")


class Handle(Stationery):
    title = "Handle"

    def draw(self):
        print("Маркер скрипит.")


my_s = Stationery()

my_pencil = Pencil()
my_pen = Pen()
my_handle = Handle()

my_s.draw()
my_pencil.draw()
my_pen.draw()
my_handle.draw()
