# We created a calculator assignment in the previous assignment. You need to update that calculator using functions. 
# Write a Python script for a calculator using functions.Create separate functions for addition, subtraction, multiplication, and division functions taking input as parameters and returning the result of the operation performed.Validate division by zero.Use input from the user to select an operation and numbers.Additionally, you can also create any more functions you like to improve the calculator functionality.

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def modulus(a, b):
    return a % b


def power(a, b):
    return a ** b


def calculator():
    print("Welcome to the Python Calculator")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (^)")

    while True:
        try:
            choice = int(input("\nEnter your choice (1-6): "))
            if choice not in range(1, 7):
                print("Invalid choice. Please choose a number between 1 and 6.")
                continue

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == 1:
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == 2:
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == 3:
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == 4:
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            elif choice == 5:
                print(f"Result: {num1} % {num2} = {modulus(num1, num2)}")
            elif choice == 6:
                print(f"Result: {num1} ^ {num2} = {power(num1, num2)}")

            # Check if the user wants to perform another calculation
            again = input("\nDo you want to perform another operation? (yes/no): ").strip().lower()
            if again != "yes":
                print("Thank you for using the calculator!")
                break

        except ValueError:
            print("Invalid input. Please enter numeric values for numbers and a valid operation choice.")


if __name__ == "__main__":
    calculator()
