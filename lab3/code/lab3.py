import pyfiglet
from colorama import Fore, Style, init
import os

# Initialize colorama
init()

def preview_ascii_art(ascii_art, color):
    """Displays a preview of ASCII art with color."""
    terminal_width = os.get_terminal_size().columns
    print("\nPreview of your ASCII Art:\n")
    # Center the preview
    formatted_preview = "\n".join(line.center(terminal_width) for line in ascii_art.splitlines())
    print(color + formatted_preview + Style.RESET_ALL)
    print("\n--- End of Preview ---\n")

def get_numeric_input(prompt, min_value=None):
    """Helper function to get a numeric input with error handling."""
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Please enter a value greater than {min_value}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")

def generate_ascii_art():
    print("Welcome to the ASCII Art Generator!")
    print("This tool lets you create ASCII art from text.")
    print("Follow the on-screen instructions to create ASCII art.\n")

    # Get user input
    text = input("Enter a word or phrase for ASCII art: ")

    # Font selection (default 'standard')
    print("\nAvailable fonts: standard, slant, 3-d, 5lineoblique")
    font = input("Choose a font for ASCII art (or leave blank for standard): ") or "standard"

    # Get desired width and height for ASCII art
    width = get_numeric_input("Enter the desired width of ASCII art (recommended above 10): ", min_value=10)
    height = get_numeric_input("Enter the desired height of ASCII art (recommended above 1): ", min_value=1)

    # Generate ASCII art
    try:
        ascii_art = pyfiglet.figlet_format(text, font=font, width=width)
    except pyfiglet.FontNotFound:
        print("The chosen font was not found. Using the default font.")
        ascii_art = pyfiglet.figlet_format(text, font="standard", width=width)

    # Scale ASCII art to the desired height
    art_lines = ascii_art.splitlines()
    scaled_art = "\n".join(line for line in art_lines for _ in range(height))

    # Terminal width for centering
    terminal_width = os.get_terminal_size().columns

    # Available colors
    colors = {
        '1': Fore.RED,
        '2': Fore.GREEN,
        '3': Fore.BLUE,
        '4': Style.RESET_ALL
    }
    print("\nAvailable colors:\n1. Red\n2. Green\n3. Blue\n4. Default (no color)")

    # Get color choice
    color = colors.get(input("Enter the color number for the text: "), Style.RESET_ALL)

    # Get character for ASCII art
    symbol = input("Enter a symbol for creating ASCII art (default '*'): ") or '*'

    # Display preview
    preview_ascii_art(ascii_art, color)

    # Rebuild ASCII art with the new symbol
    final_ascii_art = '\n'.join(
        ''.join(symbol if c != ' ' else ' ' for c in line)
        for line in scaled_art.splitlines()
    )

    # Center the final ASCII art
    centered_final_art = "\n".join(line.center(terminal_width) for line in final_ascii_art.splitlines())

    print(f"\nYour ASCII art with the symbol '{symbol}':\n")
    print(color + centered_final_art + Style.RESET_ALL)

    # Ask if user wants to save to a file
    if input("Would you like to save the ASCII art to a file? (yes/no): ").strip().lower() in ['yes', 'y']:
        filename = input("Enter file name (without extension, e.g., 'ascii_art'): ") + '.txt'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(final_ascii_art)
        print(f"ASCII art saved to file: {filename}")

    print("\nThank you for using the ASCII Art Generator! Goodbye!")

# Run the function
generate_ascii_art()
