# Smart Calculator (Basic Version)
# -----------------------------------
# This calculator performs basic arithmetic operations:
# +, -, *, /, %, and ** (power)

"""
Author: Rishi Chauhan
Date: 5 June 2025
Project: Smart CLI Calculator using Python
Version: 1.0 (Basic)
"""

print("Welcome to Smart Calculator!")

while True:
    #  Taking user input
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, **, %, /): ")
    num2 = float(input("Enter second number: "))

    #  Performing operations
    if op == "+":
        print("Result:", num1 + num2)
    elif op == "-":
        print("Result:", num1 - num2)
    elif op == "*":
        print("Result:", num1 * num2)
    elif op == "**":
        print("Result:", num1 ** num2)
    elif op == "%":
        print("Result:", num1 % num2)
    elif op == "/":
        if num2 != 0:
            print("Result:", round(num1 / num2, 2))
        else:
            print("Error: Cannot divide by zero!")
    else:
        print("Invalid operator!")

    #  Asking user if they want to continue
    again = input("Do you want to perform another calculation? (yes/no): ")
    if again.lower() != "yes":
        print("Exiting Calculator. Goodbye!")
        break
