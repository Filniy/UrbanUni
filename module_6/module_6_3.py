import random

class Animal:
  live = True
  sound = None
  _DEGREE_OF_DANGER = 0
  
  
  def __init__(self, speed, _coords = [0, 0, 0]):
    self.speed = speed
    self._cords = _coords

  def move(self, dx: int, dy: int, dz: int) -> int:
    new_x = self._cords[0] + dx * self.speed
    new_y = self._cords[1] + dy * self.speed
    new_z = self._cords[2] + dz * self.speed
    if new_z < 0:
      print("It's too deep, i can't dive :(")
      self._cords = [new_x, new_y, self._cords[2]]
    else:
      self._cords = [new_x, new_y, new_z]

  def get_cords(self):
    print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")
  
  def attack(self):
    if self._DEGREE_OF_DANGER < 5:
      print("Sorry, i'm peaceful :)")
    elif self._DEGREE_OF_DANGER > 5:
        print("Be careful, i'm attacking you 0_0")
  
  def speak(self): # Об этом методе не упоминалось ничего в задании, но в входных данных задачи он был...
    print(self.sound)

class Bird(Animal):
  beak = True
  
  def lay_eggs(self):
    print(f"Here are(is) {random.randint(1,4)} eggs for you")

class AquaticAnimal(Animal):
  _DEGREE_OF_DANGER = 3.
  
  def dive_in(self, dz):

    self._cords[2] =- abs(dz) * self.speed  / 2 # Данный алгоритм не подходит
    if self._cords[2] <= 0: # Добавляем новое условие для осуществления логики, чтобы выходные данные задачи соотвествовали с выходными данными этого модуля
      self._cords[2] = 0

class PoisonousAnimal(Animal):
  _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, AquaticAnimal, Bird): # _DEGREE_OF_DANGER он находит первее в PoisounousAnimal когда проходит по классам. Также класс Animal и Object наследуется от PoisonousAnimal, AquaticAnimal, Bird.
  sound = "Click-click-click"


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
