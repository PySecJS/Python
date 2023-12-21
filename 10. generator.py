def generator(d):
    for i in d:
        print("generator is {}".format(i))
        yield i*2

for j in generator(range(1, 5)):
    print(j)


# b = generator(range(1, 5))
# c = next(b)
# while c:
#     print(c)
#     try:
#         c = next(b)
#     except:
#         break