class House:
    #Добавление атрибута класса
    houses_history = [] #атрибут будет хранить названия созданных объектов
    
    #Контроль создания объектов
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0]) # Добавление элемента в начало списка атрибута houses_history класса House
        # print(*cls.houses_history) # вывод распакованного списка
        return super().__new__(cls) # использование метода __new__ из класса object, чтобы вернуться к тому классу, который мы испольем сейчас.
    #Запуск создания объекта класса
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    #Предыдущие методы класса Human до module_5_3.py
    def go_to(self, new_floor):
        if new_floor <= self.number_of_floors:
            for i in range(1, new_floor+1):
                print(i)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors
    
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"
    
    #Добавленные спецальные методы класса в module_5_3.py
    ## Переопределенные спецальные методы сравнения
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors
    
    ## Переопределённые спецальные методы добавления
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):
        return self.__add__(value)
    
    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self
    # Спецальный переопределенный метод, который добавлен в объект класса после module_5_4.py
    ## Переопределенный спецальный метод удаления объекта
    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")
    
    

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
