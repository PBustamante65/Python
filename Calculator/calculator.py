import math

def sum(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
def nei(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        else:
            print("Input cannot be blank. Please try again.")
def show_input():
    while True:
        if user_input == '1':
            return "Sumation"
        elif user_input == '2':
            return "Subtract"
        elif user_input == '3':
            return 'Multiply'
        elif user_input == '4':
            return 'Divide'
        elif user_input == '5':
            return 'Square root'
        elif user_input == '6':
            return 'Power of a number'
        elif user_input == '7':
            return 'Sine of an angle'
        elif user_input == '8':
            return "Cosine of an angle"
        elif user_input == "9":
            return 'Tangent of an angle'
        elif user_input == '10':
            return "Exit"

while True:
    print("-------------------")
    print("Please select one of the following options:\n")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    print('5) Square root')
    print('6) Power of a number')
    print('7) Sine of an angle')
    print('8) Cosine of an angle')
    print('9) Tangent of a angle')
    print("10) Exit")
    print("-------------------\n")

    user_input = nei(": ").lower()
    print(show_input())

    if user_input == '6':
        break

    if user_input in ('1', '2','3','4','6'):
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
    
        if user_input == '1':
            print('\nResult:', sum(num1, num2))
        elif user_input == '2':
            print('\nResult:', subtract(num1,num2))
        elif user_input == '3':
            print('\nResult:', multiply(num1,num2))
        elif user_input == '4':
            print('\nResult:', divide(num1,num2))
        elif user_input == "6":
            print("\nResult: ", math.pow(num1,num2))

    if user_input in ('5','7','8','9'):
        num3 = float(input("\nEnter the number: "))

        if user_input == '5':
            print("\nResult :", math.sqrt(num3))
        elif user_input == "7":
            print("\nResult: ", math.sin(num3))
        elif user_input == "8":
            print("\nResult: ", math.cos(num3))
        elif user_input == "9":
            print("\nResult: ", math.tan(num3))
            