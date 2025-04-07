# main.py

import my_module

name = input("Enter your name: ")
print(my_module.greet(name))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("The sum is:", my_module.add(a, b))
