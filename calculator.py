def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
# raises an error instead of crashing
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def show_menu():
    print("\n===== Calculator Master =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Select an option (1-5): ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        if choice not in ("1", "2", "3", "4"):
            print("Invalid option. Please choose a number from 1 to 5.\n")
            continue
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        try:
            if choice == "1":
                result = add(num1, num2)
                op = "+"
            elif choice == "2":
                result = subtract(num1, num2)
                op = "-"
            elif choice == "3":
                result = multiply(num1, num2)
                op = "*"
            else:  # choice == "4"
                result = divide(num1, num2)
                op = "/"

            result = round(result, 2)
            print(f"Result: {num1} {op} {num2} = {result}\n")

        except ZeroDivisionError as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()