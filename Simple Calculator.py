def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def division(x,y):
    if y==0:
        return "Error! Divisible by zero cannot be performed"
    else:
        return x/y
    
def calculator():
    print("Select Operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Division")

    while True:
        choice=input("Enter your choices (1/2/3/4): ")

        if choice in ['1','2','3','4']:
            num1=float(input("Enter first number: "))
            num2=float(input("Enter second number: "))

            if choice=='1':
                print(f'{num1}+{num2}={add(num1,num2)}')
            if choice=='2':
                print(f'{num1}-{num2}={subtract(num1,num2)}')
            if choice=='3':
                print(f'{num1}*{num2}={multiply(num1,num2)}')
            if choice=='4':
                print(f'{num1}/{num2}={division(num1,num2)}')

        next_calculation=input("Next calculation (yes/no): ")
        if next_calculation != 'yes':
            break
    print("exit calculator.ByeBye!")

calculator()

