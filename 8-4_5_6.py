import re
from re import fullmatch


class ElectronicStore:
    store = {"Printer": [], "Scanner": [], "Xerox": []}

    def put_device(self, dev):
        if dev.__class__.__base__.__name__ == "ElectronicDevice":
            self.store[dev.__class__.__name__].append(dev)
            return (len(self.store[dev.__class__.__name__]), dev.serial_num)
        else:
            print("Наш склад только для электроники!!!")
            return (None, None)

    def get_device(self, serial_num):
        for t in self.store.values():
            #           for d in self.store[t]:
            for sn in t:
                if sn.serial_num == serial_num:
                    return t.pop(t.index(sn))

        print("Устройство с таким номером отсуствует на складе")
        return None


class ElectronicDevice:

    def __init__(self, serial_num, voltage=220):
        self.voltage = voltage
        self.serial_num = serial_num


class Printer(ElectronicDevice):

    def __init__(self, serial_num, max_sheet=100):
        super().__init__(serial_num)
        self.max_sheet = max_sheet


class Scanner(ElectronicDevice):

    def __init(self, serial_num, type_of_lamp="Color"):
        super().__init__(serial_num)
        self.type_of_lamp = type_of_lamp


class Xerox(ElectronicDevice):

    def __init(self, serial_num, speed=50):
        super().__init__(serial_num)
        self.speed = speed


my_store = ElectronicStore()

depts = {"IT": [], "Another depts": []}

x1 = Xerox("020-00-01")
x2 = Xerox("818-92-03", 77)

p1 = Printer("721-34-56", 110)
p2 = Printer("132-34-00")

s1 = Scanner("000-00-11")

my_store.put_device(x1)
my_store.put_device(s1)
my_store.put_device(p2)
my_store.put_device(p1)

print(my_store.store)
print(depts)

depts["IT"] = my_store.get_device(p1.serial_num)

print(my_store.store)
print(depts)

print("Введите серийный номер устройства в формате NNN-NN-NN для извлечения из склада: ")

while True:
    sn1 = input()
    if re.fullmatch(r'\d\d\d-\d\d-\d\d', sn1):
        x3 = my_store.get_device(sn1)
        print(x3)
        print(my_store.store)
    elif sn1 == "Q":
        break
    else:
        print("Вы неверно ввели номер устройства, попробуйте еще раз, для выхода введите Q")
