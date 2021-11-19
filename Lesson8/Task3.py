# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка
#Again

class MyError(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.my_list = []

    def check_value(self):
        ex = ""
        while True:
            try:
                try:
                    user_nums = str(input('Введите числа списком через пробел или по одному: '))
                    user_set = user_nums.split()
                    for i in range(len(user_set)):
                        number = int(user_set[i])
                        print(f"Добавлен {number}")
                        self.my_list.append(number)
                    ex = input("Для выхода введите stop:").lower()
                    if ex == "stop":
                        print(self.my_list)
                        break
                except ValueError:
                    raise MyError
            except MyError:
                if ex == 'stop':
                    print(self.my_list)
                    break
                else:
                    self.check_value()


a = TypeCheck()
a.check_value()