def add(a, b):
    return a + b


# Subtraction
def subtract(a, b):
    return a - b


# Multiplication
def multiply(a, b):
    return a * b


# Division
def divide(a, b):
    return a / b


# Main Calculator Program
while True:

    print("\n================================")
    print("       PYTHON CALCULATOR")
    print("================================")

    print("\n1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("\nChoose an operation (1-5): ")

    if choice == "5":
        print("\nThank you for using Python Calculator!")
        break

    elif choice not in ["1", "2", "3", "4"]:
        print("Invalid choice! Please try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    except ValueError:
        print("Please enter valid numbers!")
        continue

    if choice == "1":
        print("Result:", add(num1, num2))

    elif choice == "2":
        print("Result:", subtract(num1, num2))

    elif choice == "3":
        print("Result:", multiply(num1, num2))

    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print("Result:", divide(num1, num2))