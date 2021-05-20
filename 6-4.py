class Car:
    speed = 0.0
    color = "RED"
    is_police = False

    def __init__(self, c="BLACK", is_p=False):
        self.speed = 0.0
        self.color = c
        self.is_police = is_p

    def go(self, s):
        self.speed = s
        print("The car is moving")
        self.show_speed()

    def stop(self):
        self.speed = 0
        print("The car is stopped")
        self.show_speed()

    def turn(self, direction):
        print(f"The car turn to {direction}")

    def show_speed(self):
        print(f"Car speed is {self.speed}")


class TownCar(Car):

    def __init__(self, c="YELLOW"):
        self.speed = 0.0
        self.color = c
        self.is_police = False

    def show_speed(self):
        if self.speed > 60.0:
            print(f"Town Car speed is too high!!!")
        else:
            print(f"Town Car speed is {self.speed}")


class SportCar(Car):
    pass

    def __init__(self, c="RED"):
        self.speed = 0.00
        self.color = c
        self.is_police = False


class WorkCar(Car):

    def __init__(self, c="WHITE"):
        self.speed = 0.0
        self.color = c
        self.is_police = False

    def show_speed(self):
        if self.speed > 40.0:
            print(f"Work Car speed is too high!!!")
        else:
            print(f"Work Car speed is {self.speed}")


class PoliceCar(Car):

    def __init__(self, c="BLACK&WHITE"):
        self.speed = 0.0
        self.color = c
        self.is_police = True


my_car = Car()

your_car = WorkCar()
those_car = TownCar()

sport_car = SportCar()

police_car = PoliceCar()

your_car.go(30)
your_car.go(90)
your_car.stop()

sport_car.go(300)
my_car.show_speed()

those_car.go(60.1)

those_car.stop()
