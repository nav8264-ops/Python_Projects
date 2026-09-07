'''Simple Calculator (If - Else)

Click run code button twice to run the code'''

try:
    n1 = float(input("Enter first number: "))
    operation = input("Enter operation (+, -, *, /): ").strip()
    n2 = float(input("Enter second number: "))

    if operation == '+':
        result = n1 + n2
        print(f"Result: {n1} + {n2} = {result}")

    elif operation == '-':
        result = n1 - n2
        print(f"Result: {n1} - {n2} = {result}")

    elif operation == '*':
        result = n1 * n2
        print(f"Result: {n1} * {n2} = {result}")

    elif operation == '/':
        if n2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = n1 / n2
            print(f"Result: {n1} / {n2} = {result}")

    else:
        print("Error: Invalid operation selected.")

except ValueError:
    print("Error: Please enter valid numeric values.")

