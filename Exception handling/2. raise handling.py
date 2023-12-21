 print("DIVISION OPERATION")
a = int(input("Enter your first value : "))
b = int(input("Enter your second value : "))

try :
    
    if b == 0:
        raise Exception("{} value Cannot divided by {}".format(a, b))      
    else :
        c = a / b
        print(c)

except Exception as e:
    print("{}".format(e))

finally :
    print("Whatever the case is work fine")

