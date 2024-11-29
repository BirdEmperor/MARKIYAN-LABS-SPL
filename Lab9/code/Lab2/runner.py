import math

# Memory for storing values
memory = None

# Calculation history
history = []

# Function to display history
def show_history():
    if history:
        print("\nCalculation history:")
        for entry in history:
            print(entry)
    else:
        print("No calculations yet.")

# Function for calculator operations
def calculate(num1, num2, operator):
    match operator:
        case '1':
            return num1 + num2
        case '2':
            return num1 - num2
        case '3':
            return num1 * num2
        case '4':
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero!"
        case '5':
            return num1 ** num2
        case '6':
            return num1 % num2
        case '7':
            return math.sqrt(num1)
        case _:
            return "Error: Invalid operator!"

# Main calculator loop
def main():
    global memory
    
    while True:
        # User input
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator((choose number) 1(+), 2(-), 3(*), 4(/), 5(^), 6(%), 7(√)): ")
        
        if operator not in ['1', '2', '3', '4', '5', '6', '7']:
            print("Invalid operator. Please enter a valid one.")
            continue
        
        # Square root doesn't need a second number
        if operator == '√':
            result = calculate(num1, None, operator)
        else:
            num2 = float(input("Enter the second number: "))
            result = calculate(num1, num2, operator)

        # Display result
        if isinstance(result, str):
            print(result)  # Show error messages
        else:
            print("Result:", result)
            history.append(f"{num1} {operator} {num2 if operator != '√' else ''} = {result}")
        
        # Memory options
        memory_option = input("Do you want to store this result in memory? (y/n): ")
        if memory_option.lower() == 'y':
            memory = result
        elif memory_option.lower() == 'recall':
            print(f"Recalled memory: {memory}")

        # Show history
        history_option = input("Do you want to view calculation history? (y/n): ")
        if history_option.lower() == 'y':
            show_history()
        
        # Repeat or exit
        repeat = input("Do you want to perform another calculation? (y/n): ")
        if repeat.lower() != 'y':
            print("Exiting calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
