#WAP in Python to swap two numbers without using a temporary variable.
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print("Before swapping: a =", a, "b =", b)
a = a + b
b = a - b
a = a - b
print("After swapping: a =", a, "b =", b)
print (a is b)
print (a is not b)
print (a is 10)