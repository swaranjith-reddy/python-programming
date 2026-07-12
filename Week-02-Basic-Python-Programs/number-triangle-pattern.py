n = int(input("Enter value of n: "))

for i in range(n, 0, -1):
    for j in range(n - i + 1):
        print(i, end="")
    print()