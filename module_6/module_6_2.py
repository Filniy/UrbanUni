class Vehicle:
    __COLOR_VARIANTS = ["Solid black",
                        'blue', 'red', 'green', 'black', 'white', 
                        "Midnight Silver Metallic", 
                        "Obsidian Black Metallic", 
                        "Deep Blue Metallic", 
                        "Silver Metallic", 
                        "Pearl White Multi-Coat",
                        "Red Multi-Coat", 
                        'Very Orange Multi-Coat', 
                        "Brilliant Yellow Multi-Coat", 
                        "Glacier Blue Multi-Coat", 
                        "Electric Blue Multi-Coat", 
                        "Green Lotus Multi-Coat"] #список допустимых цветов для окрашивания

    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
    def get_model(self):
        return f"Мощность двигателя: {self.__model}"
    
    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"
    
    def get_color(self):
        return f"Цвет: {self.__color}"
    
    def print_info(self):
         print(self.get_model(),
               self.get_horsepower(), 
               self.get_color(), 
               f"Владелец: {self.owner}")
    
    def set_color(self, new_color: str):
            new_color = new_color.lower()
            if new_color in self.__COLOR_VARIANTS:
                self.__color = new_color.upper()
            else:
                print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    
# vehicle1 = Vehicle("Arseniy", "Tesla Roadster", 248, "Green Lotus Multi-Coat")
# vehicle1.print_info()
# vehicle1.set_color('Pink')
# vehicle1.set_color('BLACK')
# vehicle1.owner = 'Vasyok'

# vehicle1.print_info()

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()