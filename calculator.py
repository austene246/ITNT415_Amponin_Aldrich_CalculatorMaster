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
        if choice == "1":
            result = add(num1, num2)
            result = round(result, 2)
            print(f"Result: {num1} + {num2} = {result}\n")
        elif choice == "2":
            result = subtract(num1, num2)
            result = round(result, 2)
            print(f"Result: {num1} - {num2} = {result}\n")
        else:
            print("Operation not yet implemented.\n")

if __name__ == "__main__":
    main()