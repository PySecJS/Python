name = input("Enter your file name or path : ")
file = open(name, 'r')

# METHOD 1
""" 
    print(file.read())
    file.close()
"""

# METHOD 2
read = file.readline()
i = 0
while read:
    read = file.readline()
    print(read)
    if i % 2 == 0:
        option = input("Read more [y/n] : ")
        if option == "n":
            print("Exit")
            break
    i = i + 1
