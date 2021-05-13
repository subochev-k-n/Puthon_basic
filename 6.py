from itertools import cycle, count

start = int(input("Введите стартовое число: "))

iter_1 = count(start)

for i in range(1, 7):
    print(next(iter_1))

neuro = ["TensorFlow", "Keras", "Theano", "VGG-16"]
iter_2 = cycle(neuro)

for i in range(1, 7):
    print(next(iter_2))
