# Рекурсия
def FOR(i):
    if i == 0:
        return 0
    i -= 1
    print(i)
    return FOR(i)


FOR(10)


# Рефлексия
class MathFunc(object):
    def square(self, n):
        return n * n

    def volume(self, n):
        return n * n * n


n = int(input("Введите число"))
name = input("Введите название функции")

obj = globals()["MathFunc"]()
data = getattr(obj, name)(n)
print(data)
