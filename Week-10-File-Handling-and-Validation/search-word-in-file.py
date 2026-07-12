def search_word(filename, word):

    with open(filename,"r") as file:
        data = file.read()

        if word in data:
            print("Word found in file")
        else:
            print("Word not found")


filename = input("Enter file name: ")
word = input("Enter word to search: ")

search_word(filename, word)
