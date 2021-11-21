# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой
#Again

class MyError(Exception):

    def __init__(self, txt):
        self.txt = txt


def div():
    try:
        num_1 = int(input('Введите число A : '))
        num_2 = int(input('Введите число B : '))
        if num_2 == 0:
            raise MyError("Деление на ноль")
        else:
            result = num_1 / num_2
            return result
    except ValueError:
        return "Вы ввели некорректное значение"
    except MyError as err:
        return err


print(div())