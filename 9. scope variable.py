a = 2

def function1():
# LOCAL VARIABLE 
    b = 3
    print("Local variable \n{}".format(b))
function1()
print(a)


def function2():
# GLOBAL VARIABLE
    global a
    a = 5
    print("Global variable \n{}".format(a))
function2()
print(a)