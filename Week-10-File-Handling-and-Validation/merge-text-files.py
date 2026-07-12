file1 = open("file1.txt","r")
file2 = open("file2.txt","r")
file3 = open("file3.txt","w")

data1 = file1.read()
data2 = file2.read()

file3.write(data1)
file3.write(data2)

file1.close()
file2.close()
file3.close()

print("Files merged successfully")
