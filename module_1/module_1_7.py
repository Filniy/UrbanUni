grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
dict={}
i = 0
for student in sorted(students):
        AV=sum(grades[i])/len(grades[i])
        dict[student] = AV
        i += 1   
print("Сортированный список:",dict)