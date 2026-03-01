import sys


class Calculator:
   
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b


def get_float_input(prompt: str) -> float:
    
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def display_menu():
    print("\nCalculator ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


def main():
    calc = Calculator()

    operations = {
        "1": calc.add,
        "2": calc.subtract,
        "3": calc.multiply,
        "4": calc.divide,
    }

    while True:
        display_menu()
        choice = input("Select an option (1-5): ")

        if choice == "5":
            print("Exiting calculator. Goodbye!")
            sys.exit()

        if choice in operations:
            num1 = get_float_input("Enter first number: ")
            num2 = get_float_input("Enter second number: ")

            try:
                result = operations[choice](num1, num2)
                print(f"Result: {result}")
            except ZeroDivisionError as error:
                print(f"Error: {error}")
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()