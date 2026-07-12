def check_ascending(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            print(False)
            return
    print(True)

lst = list(map(int, input("Enter list elements: ").split()))
check_ascending(lst)
