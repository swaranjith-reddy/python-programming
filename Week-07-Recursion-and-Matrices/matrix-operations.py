rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Enter element [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)

print("Matrix is:")

for r in matrix:
    for c in r:
        print(c, end=" ")
    print()




#The following one let's you give the input of each row at a time


# ex.Enter number of rows: 3
#Enter number of columns: 3

#Enter row elements: 1 2 3
#Enter row elements: 4 5 6
#Enter row elements: 7 8 9

"""rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []                          

for i in range(rows):
    row = list(map(int, input("Enter row elements: ").split()))
    matrix.append(row)

print("Matrix is:")

for r in matrix:
    print(r)"""