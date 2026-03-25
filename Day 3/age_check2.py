#WAP in Python to check whether the entered age is a toddler,child,teenager or adult
age = int(input("Enter age: "))
if (age<=5):
    print("You are a toddler!")
elif (age>5 and age<= 11):
    print("You are a child!")
elif (age>11 and age<= 19):
    print("You are a teenager!")
else:
    print("You are an adult!")