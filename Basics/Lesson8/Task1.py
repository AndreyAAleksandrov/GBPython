# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
#Again

from datetime import date

class Data:

    def __init__(self, data):
        self.data = data.split('-')

    @classmethod
    def type(cls, data):
        try:
            day, month, year = [int(i) for i in data.split('-')]
            return f"{type(day), day}\n{type(month), month}\n{type(year), year}"
        except ValueError:
            return 'Дата введена неверно'

    @staticmethod
    def validation(data):
        try:
            day, month, year = data.split('-')
            date(int(year), int(month), int(day))
            return 'Дата введена верно'
        except ValueError:
            return 'Дата введена неверно'

print(Data.validation('07-11-2021'))
print(Data.validation('07-15-2021'))
print("*"*100)
print(Data.type('25-02-2021'))
print(Data.type('25-02'))