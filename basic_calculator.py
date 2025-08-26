def add(x, y):
    """Function to add two numbers."""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers."""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers."""
    return x * y

def divide(x, y):
    """Function to divide two numbers."""
    if y == 0:
        return "Error: Division by zero is not allowed."  # Handle division by zero
    return x / y

def main():
    """Main function to run the calculator."""
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    while True:
        choice = input("Enter choice (1/2/3/4) or 'q' to quit: ").strip()  # Get user choice
        
        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break  # Exit the loop if user wants to quit
        
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))  # Get first number
                num2 = float(input("Enter second number: "))  # Get second number
            except ValueError:
                print("Invalid input. Please enter numeric values.")  # Handle non-numeric input
                continue
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")  # Perform addition
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")  # Perform subtraction
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")  # Perform multiplication
            elif choice == '4':
                result = divide(num1, num2)  # Perform division
                print(f"{num1} / {num2} = {result}")  # Display result
        else:
            print("Invalid choice. Please select a valid operation.")  # Handle invalid operation choice

if __name__ == "__main__":
    main()  # Run the main function when the script is executed
