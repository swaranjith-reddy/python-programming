def palindrome(str):
    if str == str[::-1]:
        print(True)
    else:
        print(False)

str = input("Enter a string: ")
palindrome(str)
