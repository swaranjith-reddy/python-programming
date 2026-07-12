def has_duplicate(lst):
    seen = []
    for item in lst:
        if item in seen:
            return True
        seen.append(item)
    return False

number = list(map(int, input("Enter Elements separated by space: ").split()))

if has_duplicate(number):
    print("List has duplicate values")
else:
    print("No duplicates in list")
