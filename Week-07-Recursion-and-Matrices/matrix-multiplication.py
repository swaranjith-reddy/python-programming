n = int(input("Enter size of square matrix: "))

A = []
B = []

print("Enter Matrix A")

for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter Matrix B")

for i in range(n):
    row = list(map(int, input().split()))
    B.append(row)

result = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            result[i][j] += A[i][k] * B[k][j]

print("Result Matrix:")

for r in result:
    print(r)













