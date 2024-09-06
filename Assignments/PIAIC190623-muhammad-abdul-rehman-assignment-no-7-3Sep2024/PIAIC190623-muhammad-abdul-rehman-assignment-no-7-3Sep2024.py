# Assignment no 7 -----------> 3 September 2024:

# Assignment Statement:

# You are tasked with creating a Python program that serves as an interactive tool for a friend who enjoys exploring numbers. The program should begin by prompting the user to enter their name and then ask them for three of their favorite numbers. After gathering this information, the program should greet the user with a personalized message that includes their name. The three numbers provided by the user should be stored in a list. The program should then check if any of the numbers are even or odd, and store this information in a separate list of tuples, where each tuple contains the number and a string indicating whether it is "even" or "odd". Following this, the program should use a for loop to iterate over the list of numbers, and for each number, it should create a tuple containing the number and its square. These tuples should be printed in a creative and engaging format. Additionally, the program should calculate the sum of the three numbers and print the result, accompanied by an encouraging message. Finally, the program should determine if the sum is a prime number and notify the user with an appropriate message. The goal is to make the tool both enjoyable and informative, allowing the user to explore their favorite numbers in a fun and interactive way, while also introducing some interesting logical checks.

# Assignment Solution:

def get_user_info():
    name = input("Hello! What's your name? ")
    favorite_numbers = []
    for i in range(3):
        while True:
            try:
                num = int(input(f"Enter your favorite number {i+1}: "))
                favorite_numbers.append(num)
                break
            except ValueError:
                print("That's not a valid number! Try again.")
    return name, favorite_numbers

def check_even_odd(numbers):
    even_odd_list = []
    for num in numbers:
        if num % 2 == 0:
            even_odd_list.append((num, "even"))
        else:
            even_odd_list.append((num, "odd"))
    return even_odd_list

def calculate_squares(numbers):
    squares = []
    for num in numbers:
        squares.append((num, num ** 2))
    return squares

def calculate_sum(numbers):
    return sum(numbers)

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def main():
    name, favorite_numbers = get_user_info()
    print(f"\nHello, {name}! Let's explore your favorite numbers:\n")
    
    even_odd_list = check_even_odd(favorite_numbers)
    print("Here are your numbers with their parity:")
    for num, parity in even_odd_list:
        print(f"{num} is {parity}")
    
    squares = calculate_squares(favorite_numbers)
    print("\nHere are your numbers with their squares:")
    for num, square in squares:
        print(f"{num} → {square}")
    
    total = calculate_sum(favorite_numbers)
    print(f"\nThe sum of your favorite numbers is: {total}")
    print("That's a great sum! Keep exploring numbers!")
    
    if is_prime(total):
        print("Wow, the sum is a prime number! That's a rare occurrence.")
    else:
        print("The sum is not a prime number, but that's okay! There's always more to explore.")

if __name__ == "__main__":
    main()