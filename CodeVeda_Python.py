"""
Simple Calculator
-----------------
A command-line based calculator that supports basic arithmetic operations:
Addition, Subtraction, Multiplication, and Division.

Features:
- Modular functions for each operation
- Error handling for invalid inputs
- Division by zero handling
"""

def add(x, y):
    """Return the sum of two numbers"""
    return x + y

def subtract(x, y):
    """Return the difference of two numbers"""
    return x - y

def multiply(x, y):
    """Return the product of two numbers"""
    return x * y

def divide(x, y):
    """Return the division result or an error message if division by zero"""
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def calculator():
    """Main function to run the calculator"""
    print("=== Simple Calculator ===")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = int(input("Enter your choice (1/2/3/4): "))
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print(f"Result: {add(num1, num2)}")
        elif choice == 2:
            print(f"Result: {subtract(num1, num2)}")
        elif choice == 3:
            print(f"Result: {multiply(num1, num2)}")
        elif choice == 4:
            print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid choice! Please select from 1 to 4.")

    except ValueError:
        print("Invalid input! Please enter valid numbers.")

if __name__ == "__main__":
    calculator()
