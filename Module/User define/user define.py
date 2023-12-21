# https://pypi.org/

a = int(input("Enter your number1 : "))
b = int(input("Enter your number2 : "))

import src.operation 
print(src.operation.add(a, b))

import src.operation as s
print(s.sub(a, b))

from src.operation import *
print(mul(a, b))

from src.operation import div
print(div(a, b))