def invert_dict(d):

    new_dict = {}
    for key in d:
        value = d[key]
        new_dict[value] = key

    return new_dict

d = {}
n = int(input("Enter number of pairs: "))
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value
result = invert_dict(d)

print("Original dictionary:", d)
print("Inverted dictionary:", result)
