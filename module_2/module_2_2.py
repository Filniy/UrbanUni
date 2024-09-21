first=int(input())
second=int(input())
third=int(input())
if first == second and second == third:
    print(3)
elif first == second or second == third or first==third:
  print(2)
elif first != second and second != third:
  print(0)