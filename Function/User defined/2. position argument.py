a = int(input("Enter your number1 : "))
b = int(input("Enter your number2 : "))
          # parameter
def hello(num1, num2):
    add = num1 + num2
    sub = num1 - num2
#   return add, sub
#   return (add, sub)
    return {
        "Add" : add,
        "Sub" : sub
    }
                                                                   # positional argument
print("The value1 {} , value2 {} and result {}".format(a, b, hello(a, b))) 