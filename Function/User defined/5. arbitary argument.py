# POSITIONAL ARGUMENT
          # parameter
def hello(a, *b):
# body of statement
    print(a)
    print(b)
    print(type(b))
# call function 
hello(1, 2, 3, 4, 5)

# KEYWORD ARGUMENT
          # parameter
def hello(c, **d):
# body of statement
    print(c)
    print(d)
    print(type(d))
# call function
hello(c=1, d=2, e=3, f=4, g=5)
