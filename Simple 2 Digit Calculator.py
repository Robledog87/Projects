def sum(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not possible"
    return x / y  # Ensure the division result is returned

print("Welcome to Calculator program")

while True:
    print("\nEnter 1 to Add")
    print("Enter 2 to Subtract")
    print("Enter 3 to Multiply")
    print("Enter 4 to Divide")
    print("Enter 5 to Exit from Calculator")

    try:
        choice = int(input("Enter your choice = "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choice == 5:
        print("Exiting the calculator. Goodbye!")
        break

    try:
        num1 = int(input("Enter first number = "))
        num2 = int(input("Enter second number = "))
    except ValueError:
        print("Invalid number input! Please enter valid integers.")
        continue

    if choice == 1:
        print("Result: ", sum(num1, num2))
    elif choice == 2:
        print("Result: ", sub(num1, num2))
    elif choice == 3:
        print("Result: ", mul(num1, num2))
    elif choice == 4:
        result = divide(num1, num2)  # We need to store the result here
        print("Result: ", result)  # Now we print the result correctly
    else:
        print("Enter valid input (1-5 only)")
