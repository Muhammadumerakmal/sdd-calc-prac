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

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from src import operations
from src import validators

# Create Rich console for enhanced output
console = Console()


def display_menu() -> None:
    """
    Display the calculator menu with all available operations.

    Prints a formatted menu showing options 1-8 for operations and 0 to exit.
    Uses Rich for enhanced visual presentation.
    """
    # Create a table for the menu
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column("Option", style="cyan bold", width=8)
    table.add_column("Operation", style="white")

    table.add_row("1", "Addition")
    table.add_row("2", "Subtraction")
    table.add_row("3", "Multiplication")
    table.add_row("4", "Division")
    table.add_row("5", "Power")
    table.add_row("6", "Square Root")
    table.add_row("7", "Percentage")
    table.add_row("8", "Modulus")
    table.add_row("", "")
    table.add_row("0", "Exit", style="red")

    # Display in a panel
    panel = Panel(table, title="[bold cyan]Calculator Menu[/bold cyan]", border_style="cyan")
    console.print()
    console.print(panel)


def get_menu_choice() -> int:
    """
    Get and validate the user's menu choice.

    Continuously prompts the user until a valid menu choice (0-8) is entered.
    Uses validators.validate_menu_choice for validation.

    Returns:
        Valid menu choice as an integer (0-8)
    """
    while True:
        user_input = console.input("\n[bold yellow]Enter your choice (0-8):[/bold yellow] ")
        is_valid, error_message = validators.validate_menu_choice(user_input)

        if is_valid:
            return int(user_input)
        else:
            console.print(f"[red]✗ Error:[/red] {error_message}")


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
        user_input = console.input(f"[bold yellow]{prompt}[/bold yellow] ")
        is_valid, error_message = validators.validate_numeric_input(user_input)

        if is_valid:
            return float(user_input)
        else:
            console.print(f"[red]✗ Error:[/red] {error_message}")


def execute_operation(choice: int) -> None:
    """
    Execute the selected mathematical operation.

    Prompts for necessary operands, calls the appropriate operation function,
    and displays the result. Handles errors gracefully (e.g., division by zero).
    Uses Rich for enhanced result presentation.

    Args:
        choice: Menu choice indicating which operation to execute (1-8)
    """
    try:
        if choice == 1:  # Addition
            a = get_numeric_input("Enter first number:")
            b = get_numeric_input("Enter second number:")
            result = operations.add(a, b)
            console.print(f"\n[green]✓ Result:[/green] [bold white]{a} + {b} = {result}[/bold white]")

        elif choice == 2:  # Subtraction
            a = get_numeric_input("Enter first number:")
            b = get_numeric_input("Enter second number:")
            result = operations.subtract(a, b)
            console.print(f"\n[green]✓ Result:[/green] [bold white]{a} - {b} = {result}[/bold white]")

        elif choice == 3:  # Multiplication
            a = get_numeric_input("Enter first number:")
            b = get_numeric_input("Enter second number:")
            result = operations.multiply(a, b)
            console.print(f"\n[green]✓ Result:[/green] [bold white]{a} × {b} = {result}[/bold white]")

        elif choice == 4:  # Division
            a = get_numeric_input("Enter first number (dividend):")
            b = get_numeric_input("Enter second number (divisor):")
            result = operations.divide(a, b)
            console.print(f"\n[green]✓ Result:[/green] [bold white]{a} ÷ {b} = {result}[/bold white]")

        elif choice == 5:  # Power
            base = get_numeric_input("Enter base:")
            exponent = get_numeric_input("Enter exponent:")
            result = operations.power(base, exponent)
            console.print(f"\n[green]✓ Result:[/green] [bold white]{base} ^ {exponent} = {result}[/bold white]")

        elif choice == 6:  # Square Root
            number = get_numeric_input("Enter number:")
            result = operations.square_root(number)
            console.print(f"\n[green]✓ Result:[/green] [bold white]√{number} = {result}[/bold white]")

        elif choice == 7:  # Percentage
            percent = get_numeric_input("Enter percentage:")
            of_value = get_numeric_input("Enter value:")
            result = operations.percentage(percent, of_value)
            console.print(f"\n[green]✓ Result:[/green] [bold white]{percent}% of {of_value} = {result}[/bold white]")

        elif choice == 8:  # Modulus
            a = get_numeric_input("Enter first number (dividend):")
            b = get_numeric_input("Enter second number (divisor):")
            result = operations.modulus(a, b)
            console.print(f"\n[green]✓ Result:[/green] [bold white]{a} mod {b} = {result}[/bold white]")

    except ValueError as e:
        console.print(f"\n[red bold]✗ Error:[/red bold] [red]{e}[/red]")


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
            console.print("\n[cyan]Thank you for using the calculator. Goodbye![/cyan]\n")
            break

        execute_operation(choice)


def main() -> None:
    """
    Main entry point for the calculator application.

    Displays welcome message, runs the main loop, and handles keyboard
    interrupts gracefully. Uses Rich for enhanced presentation.
    """
    # Welcome message with Rich styling
    welcome_panel = Panel(
        "[bold white]A modern command-line calculator with Rich UI[/bold white]\n"
        "[dim]Perform accurate mathematical calculations with style[/dim]",
        title="[bold cyan]Welcome to Calculator[/bold cyan]",
        border_style="cyan"
    )
    console.print()
    console.print(welcome_panel)

    try:
        main_loop()
    except KeyboardInterrupt:
        console.print("\n\n[yellow]Calculator interrupted. Goodbye![/yellow]")
        sys.exit(0)


if __name__ == "__main__":
    main()
