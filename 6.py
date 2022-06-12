#Simple Calculator

#Addition
def add(num1, num2):
        return num1 + num2

#Subtraction
def subtract(num1, num2):
        return num1 - num2

#Multiplication
def multiply(num1, num2):
        return num1 * num2

#Division
def divide(num1, num2):
        return num1 / num2

#Modulus
def modulus(num1, num2):
        return num1 % num2

#Ask user to select operator
operator = input("Select an operator: '+' '-' '*' '/' '%' \n")

#Ask user to input operands
num1 = float(input("Enter first number: \n"))

num2 = float(input("Enter second number: \n"))

if (operator == '+'):
    print(add(num1, num2))

elif (operator == '-'):
    print(subtract(num1, num2))

elif (operator == '*'):
    print(multiply(num1, num2))

elif (operator == '/'):
    print(divide(num1, num2))

elif (operator == '%'):
    print(modulus(num1, num2))

else:
    int(input("Enter a valid operator: '+' '-' '*' '/' '%'\n"))
