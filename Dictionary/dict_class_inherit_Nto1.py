# https://python-scripts.com/object-oriented-programming-in-python
# Player --> MobilePhone
# Navigator --> MobilePhone
# player_method --> MobilePhone
# navigator_method --> MobilePhone

class Player:
    def player_method(self):
        print("Родительский метод класса Player")

class Navigator:
    def navigator_method(self):
        print("Родительский метод класса Navigator")

class MobilePhone(Player, Navigator):
    def mobile_phone_method(self):
        print("Дочерний метод класса MobilePhone")

m_p = MobilePhone()
m_p.player_method()
m_p.navigator_method()
m_p.mobile_phone_method()

# Shape --> Triangle
# Material --> Triangle
# param_1, param_2 Shape --> VVV Triangle used super().__init__(param_1, param_2)
# param_1, param_2 Material --> XXX Triangle used super().__init__(param_1, param_2)

class Shape:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    def get_params(self):
        return f"Параметры Shape: {self.param_1} {self.param_2}"

class Material:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    def get_params(self):
        return f"Параметры Material {self.param_1} {self.param_2}"

class Triangle(Shape, Material):
    def __init__(self, param_1, param_2):
        super().__init__(param_1, param_2)
        pass

t = Triangle(100, 200)
print(t.get_params())