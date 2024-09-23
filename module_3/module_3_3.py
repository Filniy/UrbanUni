def print_params(a = 1, b = 'строка', c = True):
  print(a,b,c)
print_params(4, 3.5, False)
print_params(3, 'привет')
print_params(2)
print_params()
print_params(b = 25) 
print_params(c = [1,2,3])
values_list = [True,1,1.0]
values_dict = {"a":True, "b":1, "c":1.0}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [2,2.0]
print_params(*values_list_2)
print_params(*values_list_2, 42)