my_dict = {'Арсений': 17, "Александр": 25, "Никита": 29}
print("///////////")
print("Модуль 1.6")
# Работа с словарём
print("Словарь:", my_dict)
print("Вывод значения словаря:", my_dict["Арсений"])
print("Вывод несуществующего значения словаря:", my_dict.get("Николай"))
my_dict.update({"Сергей": 26, "Людмила": 44})
print("Вывод обновлённого словаря:", my_dict)
deleted_age_from_dict = my_dict.pop("Людмила")
print("Вывод удалённого значения из словаря:", deleted_age_from_dict)
# Работа с множеством
print("Просмотр словаря после удаления значения:", my_dict)
my_set={1,
    1,
    1,
    2,
    2,
    2,
    3,
    3,
    3,
    4,
    4,
    4,
    5,
    5,
    5,
    6,
    "String",
    True,
    (1,2,3),
    (1,2,3)}
print("Вывод множества:",my_set)
my_set.remove(1)
print("Вывод множества с удалённым уникальным значением:",my_set)
print("///////////")
# my_set=(1,
#     1,
#     1,
#     2,
#     2,
#     2,
#     3,
#     3,
#     3,
#     4,
#     4,
#     4,
#     5,
#     5,
#     5,
#     6,
#     "String",
#     True,
#     (1,2,3),
#     (1,2,3))
# print(set(my_set))
