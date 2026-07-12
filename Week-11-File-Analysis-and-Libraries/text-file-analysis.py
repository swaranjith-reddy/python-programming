def file_analysis(filename):

    file = open(filename,"r")
    data = file.read()

    words = len(data.split())

    vowels = 0
    spaces = 0
    lower = 0
    upper = 0

    for ch in data:

        if ch.lower() in "aeiou":
            vowels += 1

        if ch == " ":
            spaces += 1

        if ch.islower():
            lower += 1

        if ch.isupper():
            upper += 1

    print("Number of Words:",words)
    print("Number of Vowels:",vowels)
    print("Number of Spaces:",spaces)
    print("Lowercase Letters:",lower)
    print("Uppercase Letters:",upper)

    file.close()


file_analysis("file.txt")
