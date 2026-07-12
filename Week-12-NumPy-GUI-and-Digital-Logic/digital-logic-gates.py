# AND Gate
def AND(a, b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0

# OR Gate
def OR(a, b):
    if a == 1 or b == 1:
        return 1
    else:
        return 0

# NOT Gate
def NOT(a):
    if a == 1:
        return 0
    else:
        return 1

# XOR Gate
def XOR(a, b):
    if a != b:
        return 1
    else:
        return 0


# Input
a = int(input("Enter first input (0 or 1): "))
b = int(input("Enter second input (0 or 1): "))

# Output
print("\nLogic Gate Results")
print("AND Gate:", AND(a,b))
print("OR Gate:", OR(a,b))
print("NOT Gate (a):", NOT(a))
print("XOR Gate:", XOR(a,b))
