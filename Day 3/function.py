def add():
    a = 10
    b = 15
    a = a + b
    print("Addition:",a)
    
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    res = add(a,b)
    print(res)