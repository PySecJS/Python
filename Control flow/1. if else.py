name = input("Enter your name : ")
age = int(input("Enter your age : "))
if age >= 18 :
    print("I am {} and {} age is eligible for vote canditate".format(name.capitalize(), age))
else :
    print("I am {} and {} age is not eligible for vote canditate".format(name.capitalize(), age))