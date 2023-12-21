a = ['Apple', 'Mango', 'Orange']
for i in a:
    print("Iterable value is {}".format(i))

for i in range(0, 10+1):
    print("Iterable value {}".format(i))

a = [
    {
        "email":"raja@gmail.com",
        "password":"12345"
    },
    {
        "email":"durai@gmail.com",
        "password":"67890"
    }
]

for i in a :
    print("Username {} and Password {}".format(i["email"], i["password"]))

