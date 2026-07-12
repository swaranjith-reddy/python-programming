word = input("Enter a word: ")

result = ""

for i in range(len(word)):
    result = result + word[i]

    if i != len(word)-1:
        result = result + ","

print(result)
