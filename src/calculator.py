def fun1(a, b):
    return a + b

def fun2(a, b):
    return a - b

def fun3(a, b):
    return a * b

def fun4(a, b):
    return a / b

if __name__ == "__main__":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(fun1(a, b))
    print(fun2(a, b))
    print(fun3(a, b))
    print(fun4(a, b))