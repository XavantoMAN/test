#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Функциональный подход. Рекурсия
def sum(ls):
    if ls == []:
        return 0

    head, *tail = ls
    return sum(tail) + head


def fillList(i, ls):
    if i == 0:
        return 0

    ls.append(fillList(i - 1, ls))
    return i


a = []
fillList(10, a)
print(a)

s = sum(a)

print("Sum: " + str(s))


# Рефлексия
class MyClassAnim(object):
    anim = "Cat"

    def GetAnim(self):
        return self.anim

    def __init__(self, *val):
        pass


class MyClassTom(object):
    name = "Tom"
    age = 45

    def GetName(self):
        return self.name

    def GetAge(self):
        return self.age

    def PrintData(self):
        print("Name:" + self.name)
        print("Age:" + str(self.age))

    def __init__(self, *val):
        self.age = val[0]
        self.name = val[1]


class_name = input("Class Name:")
method = input("Function Name:")
nameP = input("Name People:")

obj = globals()[class_name](50, nameP)
data = getattr(obj, method)()

if data != None:
    print(data)
