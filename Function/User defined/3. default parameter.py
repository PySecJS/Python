a = int(input("Enter your number1 : "))
                # default value
def hello(num1, num2 = 5):
    add = num1 + num2
    sub = num1 - num2
    return {
        "Add" : add,
        "Sub" : sub
    }
                        
print("{}".format(hello(a))) # positional argument