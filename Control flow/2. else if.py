name = input("Enter your name : ")
age = int(input("Enter your age : "))
if age >= 1 and age <= 11 :
    print("I am {} and {} age prority status is babies".format(name.capitalize(), age))
elif age >= 12 and age <= 19 :
    print("I am {} and {} age prority status is teenagers".format(name.capitalize(), age))
elif age >= 20 and age <= 50 :
    print("I am {} and {} age prority status is adult or high".format(name.capitalize(), age))
elif age <= 0 :
    print("I am {} and {} age prority status is invalid age".format(name.capitalize(), age))
else :
    print("I am {} and {} age prority status is older".format(name.capitalize(), age))