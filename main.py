#
class StepValueError(ValueError):
    pass

# Создайте класс Iterator, который обладает следующими свойствами:
class Iterator():

# __init__ (self, start, stop, step=1) - принимающий значения старта и конца итерации, а также шага.
# В этом методе в первую очередь проверяется step на равенство 0.
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')

        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

#метод сбрасывающий значение pointer на start и возвращающий сам объект итератора
    def __iter__(self):
        self.pointer = self.start
        return self
#метод увеличивающий атрибут pointer на step
    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration
        current = self.pointer
        self.pointer += self.step
        return current


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print("Шаг не может быть равен 'O'")

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()