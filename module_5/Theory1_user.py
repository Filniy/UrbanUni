class User:
    __instance = None

    def __new__(cls,*args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self, *args, **kwargs):
        self.args = args
        # self.kwargs = kwargs#.get("name")
        for key, values in kwargs.items():
            setattr(self, key, values)


other = [1,2,3]
userData0 = {"name": "Den", "age": 25, "gender": "male"}
userData1 = {"name": "Filniy", "age": 17, "gender": "female"}

user0 = User(*other, **userData0)
user1 = User(*other, **userData1)
print(user0.gender)
print(user0.name)
print(user0.age)

print(user1.gender)
print(user1.name)
print(user1.age) #happens cause in pattern singleton we can only have one object at same memeory address