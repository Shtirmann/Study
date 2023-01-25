def calculator():
    while True:
        # Get the user's input
        operation = input("Enter an operation (+, -, *, /): ")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform the calculation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        else:
            result = "Invalid operation"

        # Print the result
        print("Result:", result)

        # Ask the user if they want to continue
        cont = input("Do you want to continue? (y/n)")
        if cont.lower() != "y":
            break

# Run the calculator
calculator()