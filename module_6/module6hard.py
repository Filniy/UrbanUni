import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)
        self.__color = list(color)
        self.filled = False

    def get_color(self) -> list:
        return list(self.__color)


    def __is_valid_color(self, r: int, g: int, b: int) -> bool:
        if not (0 <= r <= 255) or not (0 <= g <= 255) or not (0 <= b <= 255):
            return False
        return True


    def set_color(self, r: int, g: int, b: int):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            return

    def __is_valid_sides (self, *sides:int)->bool:
        for side in sides:
            if isinstance(side, int) and side > 0:
                if len(sides) == len(self.__sides):
                    return True
            else:
                return False

    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
            return sum(self.__sides)


    def set_sides(self, *new_sides):
        if len(new_sides) != self.sides_count :
            return
        else:
            for side in new_sides:
                self.__sides = [side]

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__radius = sides / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2
    
class Triangle(Figure):
    sides_count = 3
    
    def __init__(self, color, sides):
        super().__init__(color, sides)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = sides * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())