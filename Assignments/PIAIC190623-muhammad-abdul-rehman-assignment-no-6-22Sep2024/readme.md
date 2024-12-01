# Python Calculator Using Functions

## Project Overview

This Python script is a calculator program that performs basic arithmetic operations using functions. Each operation (addition, subtraction, multiplication, division, modulus, and power) is encapsulated in its own function for modularity and reusability.

---

## Features

1. **Basic Operations**:
   - Addition (+)
   - Subtraction (-)
   - Multiplication (*)
   - Division (/)
   - Modulus (%)
   - Power (^)

2. **Division by Zero Validation**:
   - Prevents division by zero and displays an appropriate error message.

3. **User-Friendly Menu**:
   - A clear and interactive menu to select operations.

4. **Modular Design**:
   - Separate functions for each operation make the code easy to read and extend.

5. **Error Handling**:
   - Handles invalid inputs for both numbers and operation selection.

---

## Example Input and Output

### Input:
```plaintext
Welcome to the Python Calculator
Select an operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Modulus (%)
6. Power (^)

Enter your choice (1-6): 1
Enter the first number: 10
Enter the second number: 5


Output:
plaintext
Copy code
Result: 10.0 + 5.0 = 15.0

Do you want to perform another operation? (yes/no): yes

Division by Zero Example:
Input:
plaintext
Copy code
Enter your choice (1-6): 4
Enter the first number: 10
Enter the second number: 0

Output:
plaintext
Copy code
Result: Error: Division by zero is not allowed.


Solution: calculator_functions.py
python
Copy code
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
README.md
markdown
Copy code
# Python Calculator Using Functions

## Project Overview

This Python script is a calculator program that performs basic arithmetic operations using functions. Each operation (addition, subtraction, multiplication, division, modulus, and power) is encapsulated in its own function for modularity and reusability.

---

## Features

1. **Basic Operations**:
   - Addition (+)
   - Subtraction (-)
   - Multiplication (*)
   - Division (/)
   - Modulus (%)
   - Power (^)

2. **Division by Zero Validation**:
   - Prevents division by zero and displays an appropriate error message.

3. **User-Friendly Menu**:
   - A clear and interactive menu to select operations.

4. **Modular Design**:
   - Separate functions for each operation make the code easy to read and extend.

5. **Error Handling**:
   - Handles invalid inputs for both numbers and operation selection.

---

## Example Input and Output

### Input:
```plaintext
Welcome to the Python Calculator
Select an operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Modulus (%)
6. Power (^)

Enter your choice (1-6): 1
Enter the first number: 10
Enter the second number: 5
Output:
plaintext
Copy code
Result: 10.0 + 5.0 = 15.0

Do you want to perform another operation? (yes/no): yes
Division by Zero Example:
Input:
plaintext
Copy code
Enter your choice (1-6): 4
Enter the first number: 10
Enter the second number: 0
Output:
plaintext
Copy code
Result: Error: Division by zero is not allowed.
How to Run the Program
Save the file as calculator_functions.py.
Open a terminal or command prompt.
Run the script:
bash
Copy code
python calculator_functions.py
Follow the interactive menu to select operations and input numbers.