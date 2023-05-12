# Import libraries
import random
import math

# Define calculator function
def calculator():
    print("Welcome to the Awesome Calculator!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Random Number")
    print("6. Square Root")
    print("7. Decimal to Binary")
    print("8. Binary to Decimal")
    print("9. Quit")
    
    # Get user input
    choice = int(input("Enter your choice (1-9): "))
    
    # Perform calculation
    if choice == 1:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 + num2
        print("The result is: ", result)
    elif choice == 2:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 - num2
        print("The result is: ", result)
    elif choice == 3:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 * num2
        print("The result is: ", result)
    elif choice == 4:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 / num2
        print("The result is: ", result)
    elif choice == 5:
        result = random.randint(1, 100)
        print("The random number is: ", result)
    elif choice == 6:
        num = int(input("Enter a number: "))
        result = math.sqrt(num)
        print("The square root of", num, "is:", result)
    elif choice == 7:
        num = int(input("Enter a decimal number: "))
        result = bin(num)
        print("The binary equivalent of", num, "is:", result)
    elif choice == 8:
        num = input("Enter a binary number: ")
        result = int(num, 2)
        print("The decimal equivalent of", num, "is:", result)
    elif choice == 9:
        print("Thank you for using the Awesome Calculator!")
        return
    else:
        print("Invalid input. Please try again.")
    
    # Ask user if they want to continue using the calculator
    restart = input("Do you want to calculate again? (yes or no): ")
    if restart.lower() == "yes":
        calculator()
    else:
        print("Thank you for using the Awesome Calculator!")

# Call calculator function
calculator()
