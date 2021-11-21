# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
# которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Clothes:
    clothsum = 0

    def __init__(self,name):
        self.name = name

    @property
    def get_info(self):
        print(f"{self.name}")

    @property
    def size(self):
        return f"{self.cloth}"


class Coat(Clothes):

    def __init__(self,name, V):
        super().__init__(name)
        self.cloth = V/6.5 + 0.5
        Clothes.clothsum = Clothes.clothsum + self.cloth


class Suit(Clothes):

    def __init__(self, name, H):
        super().__init__(name)
        self.cloth = 2*H + 0.3
        Clothes.clothsum = Clothes.clothsum + self.cloth


clothes_1 = Coat("Пальто 1", 130)
clothes_2 = Suit("Костюм 1", 15)
clothes_3 = Coat("Пальто 2", 143)

clothes_1.get_info
print(clothes_1.size)

clothes_2.get_info
print(clothes_2.size)

clothes_3.get_info
print(clothes_3.size)

print(clothes_1.clothsum)
print(Clothes.clothsum)