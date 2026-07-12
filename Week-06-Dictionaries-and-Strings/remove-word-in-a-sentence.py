sentence = input("Enter a sentence: ")
word = input("Enter the word to remove: ")

result = ""

words = sentence.split()

for w in words:
    if w != word:
        result = result + w + " "

print("Updated sentence:", result)
