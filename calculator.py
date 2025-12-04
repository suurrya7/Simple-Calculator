"""
Simple command-line calculator.

Functions:
- add(x, y)
- subtract(x, y)
- multiply(x, y)
- divide(x, y)

Run this file directly to use the interactive calculator.
"""


def add(x: float, y: float) -> float:
    """Return the sum of two numbers."""
    return x + y


def subtract(x: float, y: float) -> float:
    """Return the difference of two numbers (x - y)."""
    return x - y


def multiply(x: float, y: float) -> float:
    """Return the product of two numbers."""
    return x * y


def divide(x: float, y: float) -> float:
    """
    Return the quotient of two numbers (x / y).

    Raises:
        ZeroDivisionError: If y is zero.
    """
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y


def run_calculator() -> None:
    """Main function to run the calculator interactively."""
    print("=== Simple Calculator ===")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("Type 'q' to quit.\n")

    while True:
        choice = input("Enter choice (1/2/3/4 or q to quit): ").strip().lower()

        if choice == "q":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please select 1, 2, 3, 4 or q.\n")
            continue

        # Get numbers from the user
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.\n")
            continue

        # Perform the calculation
        try:
            if choice == "1":
                op_symbol = "+"
                result = add(num1, num2)
            elif choice == "2":
                op_symbol = "-"
                result = subtract(num1, num2)
            elif choice == "3":
                op_symbol = "*"
                result = multiply(num1, num2)
            else:  # choice == "4"
                op_symbol = "/"
                result = divide(num1, num2)

            print(f"\nResult: {num1} {op_symbol} {num2} = {result}\n")

        except ZeroDivisionError as e:
            print(f"Error: {e}\n")
            continue

        # Ask if user wants another calculation
        next_calculation = input("Do you want to do another calculation? (yes/no): ").strip().lower()
        if next_calculation not in ("yes", "y"):
            print("Exiting calculator. Goodbye!")
            break
        print()  # blank line for readability


if __name__ == "__main__":
    run_calculator()
