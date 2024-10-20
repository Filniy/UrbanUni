class Human: # Создание класса Человек

    # Атрибуты класса Human
    ## Создание общих атрибутов для всех экземпляров класса
    head = True # Константные атрибуты объекта 
    
    # # Pattern Singleton
    # __instance = None ## Спецальный классовый атрибут
    # ### Спеацльный метод - конструктор
    # #### Использвоание методов родительского класса в дочернем классе, чтобы гарантировать использование одного созданного объекта на протяжении всей работы программы
    # def __new__(cls, *args, **kwargs):
    #     if cls.__instance is None:
    #         cls.__instance = super().__new__(cls) 
    #     return cls.__instance

    # Спецальный метод - конструктор
    ## Создание атрибутов и методов для объекта класса 
    def __init__(self, name, age): #Определяем класс, чтобы создавать уникальные объекты на основе его
        self.age = age
        self.name = name

    # Созданный метод birthday объекта класса Human
    def birthday(self): # Создание метода birthday для экзепляра класса
        self.age += 1
        print(f"{self.name} теперь {self.age} года! ☺")
    #Перегрузка 
    def __str__(self): # # Изменинение поведения спецального метода len для того, чтобы узнать информацию о человеке
        return f"Имя человека: {self.name}, лет человеку: {self.age}."
    
    def __len__(self): # Изменинение поведения спецального метода len для того, чтобы узнать кол-во лет человека
        return self.age

    def __lt__(self, other): # Изменинение поведения спецального метода сравнения lower than
        print(f"{self.age} < {other.age}?")
        return self.age < other.age 
    
    def __gt__(self, other): # Изменинение поведения спецального метода сравнения greater than
        print(f"{self.age} > {other.age}?")
        return self.age > other.age 
    
    def __eq__(self, other): # Изменинение поведения спецального метода сравнения equal
        print(f"{self.age} == {other.age}?")
        return self.age == other.age
    
# Определяем объекты 
Den = Human("Den", 21)
Max = Human("Max", 22)

print(Den.head) # Общие атрибуты всех объектов класса Human
print(Den)
print(Max)

# Длина того сколько человек прожил лет 
print(len(Den))
print(len(Max))

# День рождения человек
Den.birthday()

#Этому человеку меньше лет чем другому человеку?
print(Den < Max)
# Этому человеку больше лет чем другому человеку?
print(Den > Max)
# Этому человеку аналогичное кол-во лет чем другому?
print(Den == Max)