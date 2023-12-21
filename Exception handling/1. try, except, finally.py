a = 10
b = [1, 2, 3, 4, 5]

try :
    c = a / b[5]
    print(c)

# except NameError as e:
#     print("NameError : {}".format(e))

# except (NameError, IndexError) as e:
#     print("{}".format(e))

except Exception as e:
    print("{}".format(e))

finally :
    print("Whatever the case is work fine")