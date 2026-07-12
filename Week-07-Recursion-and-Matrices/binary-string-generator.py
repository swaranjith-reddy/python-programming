def generate_binary(n, binary=""):

    if len(binary) == n:
        print(binary)
        return
    generate_binary(n, binary + "0")
    generate_binary(n, binary + "1")

n = int(input("Enter number of bits: "))
generate_binary(n)
