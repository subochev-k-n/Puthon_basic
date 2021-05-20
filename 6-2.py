class Road:
    _lentgh = 0.0
    _width = 0.0

    def __init__(self, l, w):
        self._lentgh = l
        self._width = w

    def fullmass(self, height):
        return self._lentgh * self._width * 25 * height


r = Road(20, 5000)
print(r.fullmass(5))
