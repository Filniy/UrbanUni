sum_string = 0
sum_number = 0
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data_structure):
  global sum_string,total,sum_number
  if isinstance(data_structure, (list, tuple, set)):
    for item in data_structure:
      calculate_structure_sum(item)
  elif isinstance(data_structure, dict):
    for value in data_structure.values():
      calculate_structure_sum(value)
    for key in data_structure.keys():
      calculate_structure_sum(key)
  elif isinstance(data_structure, (int, float)) or isinstance(data_structure, str):
    if isinstance(data_structure, (int, float)):
      sum_number += data_structure
    if isinstance(data_structure, str):
      sum_string += len(data_structure)
      
  return sum_number + sum_string
print(calculate_structure_sum(data_structure))
