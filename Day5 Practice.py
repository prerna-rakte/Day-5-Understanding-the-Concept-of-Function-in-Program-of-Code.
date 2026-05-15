def name():
    print("Python Programming")

name()

def add(num1, num2):
    print ("Addition: ",num1 + num2)

add(10,20)

def add(num1, num2):
    return num1 + num2
x = add(10,20)
y = x * 2
print("Addition of numbers: ",x)
print(x,"multiply by 2: ",y)

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial of Number: ", fact)
factorial(4)

def factorial():
    num= int(input("Enter value of number: "))
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial of Number: ", fact)
factorial()

def prime(num):
    count= 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print("Prime Number")
    else:
        print("Not Prime Number")

prime(7)


def prime():
    num = int(input("Enter your number: "))
    count= 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print("Prime Number")
    else:
        print("Not Prime Number")

prime()

def add(num1, num2):
    print("Addition: ", num1 + num2)

def sub(num1, num2):
    print("Subtraction: ", num1 - num2)

def mul(num1, num2):
    print("Multiplication: ", num1 * num2)

def div(num1, num2):
    if num2 == 0:
        print("Not Divisble by Zero")
    else:
        print("Division: ", num1 / num2)

add(10,5)
sub(10,5)
mul(10,5)
div(10,5)