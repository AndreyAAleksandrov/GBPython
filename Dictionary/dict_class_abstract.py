from abc import ABC, abstractmethod

class ParentClass(ABC):
    @abstractmethod
    def method_1(self):
        print("Parent 1")

    @abstractmethod
    def method_2(self):
        print("Parent 2")

    def method_3(self):
        print("Parent 3")

    def method_4(self):
        print("Parent 4")

class DoughterClass(ParentClass):
    def method_1(self):
        print("Doughter 1")

    def method_3(self):
        print("Doughter 3")

a = DoughterClass()
a.method_1()
a.method_2()
# Не запустит пока не закомментим строку 8 или не внесем method_2 в Doughter
a.method_3()
a.method_4()