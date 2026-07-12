with open("words.txt", "r") as file:
    words = file.read().split()

words += ['l','a','']

with open("words.txt", "w") as file:
    file.write(" ".join(words))   # add space between words

print("Updated file:")
print(words)
