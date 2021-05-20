from time import sleep


class TrafficLight:
    __color = "red"

    def running(self):
        print(self.__color)
        if self.__color == "red":
            sleep(7)
            self.__color = "yellow"
        else:
            if self.__color == "yellow":
                sleep(2)
                self.__color = "green"
            else:
                sleep(5)
                self.__color = "red"


tl1 = TrafficLight()
i = 0
while i < 9:
    tl1.running()
    i += 1
