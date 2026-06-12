"""
Calculator CLI application.

This module provides the command-line interface for the Calculator application.
It handles user interaction, menu display, input collection, operation execution,
and error handling.

Functions:
    display_menu: Display the calculator menu
    get_menu_choice: Get and validate user's menu choice
    get_numeric_input: Get and validate numeric input from user
    execute_operation: Execute the selected operation
    main_loop: Main application loop
    main: Application entry point
"""

import sys
from typing import Optional

from src import operations
from src import validators


def display_menu() -> None:
    """
    Display the calculator menu with all available operations.

    Prints a formatted menu showing options 1-8 for operations and 0 to exit.
    """
    print("\n" + "=" * 50)
    print("Calculator Menu".center(50))
    print("=" * 50)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Percentage")
    print("8. Modulus")
    print("0. Exit")
    print("=" * 50)


def get_menu_choice() -> int:
    """
    Get and validate the user's menu choice.

    Continuously prompts the user until a valid menu choice (0-8) is entered.
    Uses validators.validate_menu_choice for validation.

    Returns:
        Valid menu choice as an integer (0-8)
    """
    while True:
        user_input = input("\nEnter your choice (0-8): ")
        is_valid, error_message = validators.validate_menu_choice(user_input)

        if is_valid:
            return int(user_input)
        else:
            print(f"Error: {error_message}")


def get_numeric_input(prompt: str) -> float:
    """
    Get and validate numeric input from the user.

    Continuously prompts the user until valid numeric input is entered.
    Uses validators.validate_numeric_input for validation.

    Args:
        prompt: The prompt message to display to the user

    Returns:
        Valid numeric input as a float
    """
    while True:
        user_input = input(prompt)
        is_valid, error_message = validators.validate_numeric_input(user_input)

        if is_valid:
            return float(user_input)
        else:
            print(f"Error: {error_message}")


def execute_operation(choice: int) -> None:
    """
    Execute the selected mathematical operation.

    Prompts for necessary operands, calls the appropriate operation function,
    and displays the result. Handles errors gracefully (e.g., division by zero).

    Args:
        choice: Menu choice indicating which operation to execute (1-8)
    """
    try:
        if choice == 1:  # Addition
            a = get_numeric_input("Enter first number: ")
            b = get_numeric_input("Enter second number: ")
            result = operations.add(a, b)
            print(f"\nResult: {a} + {b} = {result}")

        elif choice == 2:  # Subtraction
            a = get_numeric_input("Enter first number: ")
            b = get_numeric_input("Enter second number: ")
            result = operations.subtract(a, b)
            print(f"\nResult: {a} - {b} = {result}")

        elif choice == 3:  # Multiplication
            a = get_numeric_input("Enter first number: ")
            b = get_numeric_input("Enter second number: ")
            result = operations.multiply(a, b)
            print(f"\nResult: {a} × {b} = {result}")

        elif choice == 4:  # Division
            a = get_numeric_input("Enter first number (dividend): ")
            b = get_numeric_input("Enter second number (divisor): ")
            result = operations.divide(a, b)
            print(f"\nResult: {a} ÷ {b} = {result}")

        elif choice == 5:  # Power
            base = get_numeric_input("Enter base: ")
            exponent = get_numeric_input("Enter exponent: ")
            result = operations.power(base, exponent)
            print(f"\nResult: {base} ^ {exponent} = {result}")

        elif choice == 6:  # Square Root
            number = get_numeric_input("Enter number: ")
            result = operations.square_root(number)
            print(f"\nResult: √{number} = {result}")

        elif choice == 7:  # Percentage
            percent = get_numeric_input("Enter percentage: ")
            of_value = get_numeric_input("Enter value: ")
            result = operations.percentage(percent, of_value)
            print(f"\nResult: {percent}% of {of_value} = {result}")

        elif choice == 8:  # Modulus
            a = get_numeric_input("Enter first number (dividend): ")
            b = get_numeric_input("Enter second number (divisor): ")
            result = operations.modulus(a, b)
            print(f"\nResult: {a} mod {b} = {result}")

    except ValueError as e:
        print(f"\nError: {e}")


def main_loop() -> None:
    """
    Main application loop for the calculator.

    Continuously displays the menu, gets user choice, and executes operations
    until the user chooses to exit (choice 0).
    """
    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == 0:
            print("\nThank you for using the calculator. Goodbye!")
            break

        execute_operation(choice)


def main() -> None:
    """
    Main entry point for the calculator application.

    Displays welcome message, runs the main loop, and handles keyboard
    interrupts gracefully.
    """
    print("\n" + "=" * 50)
    print("Welcome to Calculator".center(50))
    print("=" * 50)

    try:
        main_loop()
    except KeyboardInterrupt:
        print("\n\nCalculator interrupted. Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
