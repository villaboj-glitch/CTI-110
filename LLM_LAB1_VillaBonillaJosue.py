# Josue VillaBonilla
# 26 APR 26
# AI Python Calculator
# This program asks the user for two numbers and an operation,
# then performs the calculation and displays the result.

print("Simple Calculator")

# Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user to choose an operation
print("Choose an operation:")
print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")

operation = input("Enter your choice: ")

# Perform the calculation
if operation == "+":
    result = num1 + num2
    print("Result:", result)
elif operation == "-":
    result = num1 - num2
    print("Result:", result)
elif operation == "*":
    result = num1 * num2
    print("Result:", result)
elif operation == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
        print("Result:", result)
else:
    print("Error: Invalid operation selected.")