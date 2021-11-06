# Shape --> Rectangle
# Shape --> Triangle
# Shape method --> Rectangle by default
# Shape method --> Triangle by default
# Shape params --> Rectangle use super().__init__
# Shape params --> Triangle use super().__init__

class Shape:
    def __init__(self, color, param_1, param_2):
        print("Аттрибуты конструктора def __init__(self, color, param_1, param_2): из родительского класса class Shape:")
        self.color = color
        self.param_1 = param_1
        self.param_2 = param_2

    def square(self):
        print("Метод def square(self): из родительского класса class Shape:")
        return self.param_1 * self.param_2

class Rectangle(Shape):
    def __init__(self, color, param_1, param_2, rectangle_p):
        print("Аттрибуты конструктора def __init__(self, color, param_1, param_2, rectangle_p): из дочернего класса class Rectangle(Shape):")
        super().__init__(color, param_1, param_2)
        self.rectangle_p = rectangle_p

    def get_r_p(self):
        print("Метод def get_r_p(self): из дочернего класса class Rectangle(Shape):")
        return self.rectangle_p

class Triangle(Shape):
    def __init__(self, color, param_1, param_2, triangle_p):
        print("Аттрибуты конструктора def __init__(self, color, param_1, param_2, triangle_p): из дочернего класса class Triangle(Shape):")
        super().__init__(color, param_1, param_2)
        self.triangle_p = triangle_p

    def get_t_p(self):
        print("Метод def get_t_p(self): из дочернего класса class Triangle(Shape):")
        return self.triangle_p

s = Shape("White", 9, 12)
print(f"{s.color} {s.param_1} {s.param_2} {s.square()} ")


r = Rectangle("Blue", 10, 10, True)
print(f"{r.color} {r.param_1} {r.param_2} {r.square()} {r.rectangle_p}")

t = Triangle("Yellow", 2, 2, False)
print(f"{t.color} {t.param_1} {t.param_2} {t.square()} {t.triangle_p}")
# square унаследован от родителя и для их ввода были использованы родителский ввод параметров


