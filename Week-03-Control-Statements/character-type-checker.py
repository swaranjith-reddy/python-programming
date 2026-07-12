ch = input("Enter a character: ")

if ch.isdigit():
    print("Digit")

elif ch.islower():
    print("Lowercase character")

elif ch.isupper():
    print("Uppercase character")

else:
    print("Special character")
