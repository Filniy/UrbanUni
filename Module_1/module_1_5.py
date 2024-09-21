immutable_var = (123,"eyes", 1.23, True)
#print(immutable_var)
print("Tuple:",immutable_var[0],immutable_var[1],immutable_var[2],immutable_var[3])
#immutable_var.extend(immutable_var)
#immutable_var.append(1,2,3,4)
#immutable_var[0] = 124
#immutable_var[1] = "nose"
#immutable_var[2] = 1.24  # COMMENT
#immutable_var[3] = False # You can't edit the tuple cause it does not
                          # support item assigment because it's supposed to be static type of data and not dynamic type
                          # of data
mutable_list = [123,"eyes", 1.23, True]
mutable_list[0] = 124
mutable_list[1] = "nose"
mutable_list[2] = 1.24
mutable_list[3] = False
print("Edited list:",mutable_list[0], mutable_list[1], mutable_list[2], mutable_list[3])
