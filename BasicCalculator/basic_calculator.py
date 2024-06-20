def add(x, y):
    """
    Add two numbers.
    """
    return x + y


def subtract(x, y):
    """
    Subtract the second number from the first number.
    """
    return x - y


def multiply(x, y):
    """
    Multiply two numbers.
    """
    return x * y


def divide(x, y):
    """
    Divide the first number by the second number.
    Return an error message if the second number is zero.
    """
    if y == 0:
        return "Error! Division by zero."
    return x / y


if __name__ == "__main__":
    # Display the available operations
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Get user input for the operation choice
    choice = input("Enter choice (1/2/3/4): ")

    # Get user input for the numbers to operate on
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the chosen operation and display the result
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input")  # Handle invalid operation choice
