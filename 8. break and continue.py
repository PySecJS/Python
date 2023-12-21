# BREAK
print("BREAK")
for i in range (1, 10):
    print("Iterable value {}".format(i))
    if i > 5-1:
        break


# CONTINUE
print("CONTINUE")
for i in range(1, 10):
    if i % 2 != 0 :
        continue
    else :
        print("Even number {}".format(i))
