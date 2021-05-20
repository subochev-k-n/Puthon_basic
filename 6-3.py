class Worker():
    name = "John"
    surname = "Doe"
    position = "peasant"
    _income = {"wage": 100, "bonus": 10}

    def __init__(self):
        pass

    def __init__(self, n="John", sn="Doe", p="peasant", i={"wage": 100, "bonus": 10}):
        self.name = n
        self.surname = sn
        self.position = p
        self._income = i


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


p1 = Position()
p2 = Position("Rosy", "Jane", "proctor", {"wage": 97, "bonus": 12})
print(p1.get_full_name())
print(p1.get_total_income())

print(p2.get_full_name())
print(p2.get_total_income())
