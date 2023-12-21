from functools import wraps

def decorator(function):
    def wrapper(num1, num2):
        if num1 < num2 :
            num1, num2 = num2, num1
        else :
            num2, num1 = num2, num1
        return function(num1, num2)
    return wrapper

@decorator
def decorativewrapper(num1, num2):
    sub = num1 - num2 
    print(sub)

decorativewrapper(9, 3)