from abc import ABC


class Clothes(ABC):

    def __init__(self, metrica):
        self.metrica = metrica

    @property
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):

    def consumption(self):
        return self.metrica / 6.5 + 0.5


class Suit(Clothes):

    def consumption(self):
        return self.metrica * 2 + 0.3


coat = Coat(650)
suit = Suit(50)
print(coat.consumption())
print(suit.consumption())
