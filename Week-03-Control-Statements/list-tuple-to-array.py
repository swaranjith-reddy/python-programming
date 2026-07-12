import array

# List
my_list = [1, 2, 3, 4, 5]

# Tuple
my_tuple = (6, 7, 8, 9, 10)

# Convert list to array
list_array = array.array('i', my_list)

# Convert tuple to array
tuple_array = array.array('i', my_tuple)

print("Array from list:", list_array)
print("Array from tuple:", tuple_array)
