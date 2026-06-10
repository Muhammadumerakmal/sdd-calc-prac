# Module Contracts: Calculator

**Feature**: Calculator  
**Date**: 2026-06-10  
**Purpose**: Define the public interfaces and contracts for all calculator modules

## Overview

This document specifies the function signatures, input/output contracts, and behavioral contracts for the Calculator application modules. Since this is a command-line application (not a web API), contracts are defined as Python function signatures with clear preconditions and postconditions.

---

## Module: operations.py

**Purpose**: Pure mathematical operation functions

**Contract Guarantees**:
- All functions are pure (no side effects, no I/O)
- Given valid inputs, always return correct mathematical results
- Invalid inputs raise ValueError with descriptive messages
- All functions are deterministic (same input → same output)

### Function: add

```python
def add(a: float, b: float) -> float:
    """
    Add two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Sum of a and b
    
    Raises:
        ValueError: If inputs cannot be processed
    
    Examples:
        >>> add(2.0, 3.0)
        5.0
        >>> add(-5.0, 10.0)
        5.0
        >>> add(0.0, 0.0)
        0.0
    """
```

**Preconditions**: a and b are valid float values  
**Postconditions**: Returns a + b  
**Edge Cases**: Handles negative numbers, zero, decimals  
**Performance**: O(1), <1ms

---

### Function: subtract

```python
def subtract(a: float, b: float) -> float:
    """
    Subtract second number from first number.
    
    Args:
        a: Number to subtract from
        b: Number to subtract
    
    Returns:
        Difference (a - b)
    
    Raises:
        ValueError: If inputs cannot be processed
    
    Examples:
        >>> subtract(10.0, 3.0)
        7.0
        >>> subtract(5.0, 10.0)
        -5.0
        >>> subtract(0.0, 0.0)
        0.0
    """
```

**Preconditions**: a and b are valid float values  
**Postconditions**: Returns a - b  
**Edge Cases**: Handles negative results, zero  
**Performance**: O(1), <1ms

---

### Function: multiply

```python
def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Product of a and b
    
    Raises:
        ValueError: If inputs cannot be processed
    
    Examples:
        >>> multiply(6.0, 7.0)
        42.0
        >>> multiply(-5.0, 3.0)
        -15.0
        >>> multiply(0.0, 100.0)
        0.0
    """
```

**Preconditions**: a and b are valid float values  
**Postconditions**: Returns a * b  
**Edge Cases**: Handles zero, negative numbers  
**Performance**: O(1), <1ms

---

### Function: divide

```python
def divide(a: float, b: float) -> float:
    """
    Divide first number by second number.
    
    Args:
        a: Dividend (number to be divided)
        b: Divisor (number to divide by)
    
    Returns:
        Quotient (a / b)
    
    Raises:
        ValueError: If b is zero (division by zero)
    
    Examples:
        >>> divide(15.0, 3.0)
        5.0
        >>> divide(7.0, 2.0)
        3.5
        >>> divide(10.0, 0.0)
        ValueError: Cannot divide by zero
    """
```

**Preconditions**: a is valid float, b is valid float and b ≠ 0  
**Postconditions**: Returns a / b  
**Edge Cases**: Division by zero raises ValueError  
**Performance**: O(1), <1ms

---

### Function: power

```python
def power(base: float, exponent: float) -> float:
    """
    Raise base to the power of exponent.
    
    Args:
        base: The base number
        exponent: The exponent
    
    Returns:
        base raised to the power of exponent (base ^ exponent)
    
    Raises:
        ValueError: If result would overflow or is undefined
    
    Examples:
        >>> power(2.0, 8.0)
        256.0
        >>> power(10.0, 3.0)
        1000.0
        >>> power(5.0, 0.0)
        1.0
        >>> power(0.0, 0.0)
        1.0
    """
```

**Preconditions**: base and exponent are valid float values  
**Postconditions**: Returns base ^ exponent  
**Edge Cases**: 0^0 returns 1.0, handles negative exponents  
**Performance**: O(1), <1ms

---

### Function: square_root

```python
def square_root(number: float) -> float:
    """
    Calculate the square root of a number.
    
    Args:
        number: The number to find square root of
    
    Returns:
        Square root of the number
    
    Raises:
        ValueError: If number is negative
    
    Examples:
        >>> square_root(16.0)
        4.0
        >>> square_root(0.0)
        0.0
        >>> square_root(2.0)
        1.4142135623730951
        >>> square_root(-9.0)
        ValueError: Square root requires a non-negative number
    """
```

**Preconditions**: number is valid float and number ≥ 0  
**Postconditions**: Returns √number  
**Edge Cases**: Negative numbers raise ValueError, zero returns zero  
**Performance**: O(1), <1ms

---

### Function: percentage

```python
def percentage(percent: float, of_value: float) -> float:
    """
    Calculate percentage of a value.
    
    Args:
        percent: The percentage (e.g., 20 for 20%)
        of_value: The value to calculate percentage of
    
    Returns:
        The calculated percentage value
    
    Examples:
        >>> percentage(20.0, 50.0)
        10.0
        >>> percentage(50.0, 100.0)
        50.0
        >>> percentage(100.0, 25.0)
        25.0
    """
```

**Preconditions**: percent and of_value are valid float values  
**Postconditions**: Returns (percent / 100) * of_value  
**Edge Cases**: Handles zero percent, zero value  
**Performance**: O(1), <1ms

---

### Function: modulus

```python
def modulus(a: float, b: float) -> float:
    """
    Calculate remainder of division (a modulo b).
    
    Args:
        a: Dividend
        b: Divisor
    
    Returns:
        Remainder of a / b
    
    Raises:
        ValueError: If b is zero
    
    Examples:
        >>> modulus(17.0, 5.0)
        2.0
        >>> modulus(10.0, 3.0)
        1.0
        >>> modulus(8.0, 4.0)
        0.0
    """
```

**Preconditions**: a and b are valid float values, b ≠ 0  
**Postconditions**: Returns a % b  
**Edge Cases**: Division by zero raises ValueError  
**Performance**: O(1), <1ms

---

## Module: validators.py

**Purpose**: Input validation functions

**Contract Guarantees**:
- All functions are pure (no side effects)
- Return (bool, str) tuples: (is_valid, error_message)
- Never raise exceptions (returns error status instead)
- Empty error message when valid

### Function: validate_numeric_input

```python
def validate_numeric_input(user_input: str) -> Tuple[bool, str]:
    """
    Validate that user input is a valid number.
    
    Args:
        user_input: Raw string input from user
    
    Returns:
        Tuple of (is_valid, error_message)
        - is_valid: True if input is valid number, False otherwise
        - error_message: Empty string if valid, error description if invalid
    
    Examples:
        >>> validate_numeric_input("42.5")
        (True, "")
        >>> validate_numeric_input("-10")
        (True, "")
        >>> validate_numeric_input("abc")
        (False, "Invalid number entered. Please enter a numeric value.")
        >>> validate_numeric_input("")
        (False, "Input cannot be empty. Please enter a value.")
    """
```

**Preconditions**: user_input is a string  
**Postconditions**: Returns validation result tuple  
**Valid Formats**: Integer ("42"), decimal ("3.14"), negative ("-5"), negative decimal ("-3.14")  
**Invalid Formats**: Empty, letters, special characters (except . and leading -)

---

### Function: validate_menu_choice

```python
def validate_menu_choice(user_input: str) -> Tuple[bool, str]:
    """
    Validate that user input is a valid menu choice (0-8).
    
    Args:
        user_input: Raw string input from user
    
    Returns:
        Tuple of (is_valid, error_message)
        - is_valid: True if input is valid menu choice, False otherwise
        - error_message: Empty string if valid, error description if invalid
    
    Examples:
        >>> validate_menu_choice("1")
        (True, "")
        >>> validate_menu_choice("8")
        (True, "")
        >>> validate_menu_choice("0")
        (True, "")
        >>> validate_menu_choice("9")
        (False, "Invalid menu choice. Please select a number from 0-8.")
        >>> validate_menu_choice("abc")
        (False, "Invalid menu choice. Please select a number from 0-8.")
    """
```

**Preconditions**: user_input is a string  
**Postconditions**: Returns validation result tuple  
**Valid Range**: 0-8 (inclusive)  
**Special**: 0 is exit option

---

### Function: validate_non_negative

```python
def validate_non_negative(number: float) -> Tuple[bool, str]:
    """
    Validate that a number is non-negative (>= 0).
    
    Args:
        number: The number to validate
    
    Returns:
        Tuple of (is_valid, error_message)
        - is_valid: True if number >= 0, False otherwise
        - error_message: Empty string if valid, error description if invalid
    
    Examples:
        >>> validate_non_negative(5.0)
        (True, "")
        >>> validate_non_negative(0.0)
        (True, "")
        >>> validate_non_negative(-5.0)
        (False, "Value must be non-negative.")
    """
```

**Preconditions**: number is a valid float  
**Postconditions**: Returns validation result tuple  
**Use Case**: Pre-validation for square_root operation

---

## Module: calculator.py

**Purpose**: Main CLI application and user interaction

**Contract Guarantees**:
- Handles all user I/O
- Never crashes on user input (catches all exceptions)
- Provides clear error messages
- Allows continuous operation until user exits

### Function: display_menu

```python
def display_menu() -> None:
    """
    Display the calculator menu to the user.
    
    Prints the menu of available operations with numbered options.
    
    Returns:
        None (outputs to stdout)
    
    Side Effects:
        Prints menu to console
    
    Example Output:
        ===== Calculator Menu =====
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Power
        6. Square Root
        7. Percentage
        8. Modulus
        0. Exit
        ===========================
    """
```

**Preconditions**: None  
**Postconditions**: Menu displayed to stdout  
**Side Effects**: Prints to console

---

### Function: get_numeric_input

```python
def get_numeric_input(prompt: str) -> float:
    """
    Get and validate numeric input from user.
    
    Args:
        prompt: The prompt message to display
    
    Returns:
        Valid float value from user
    
    Behavior:
        Continues prompting until valid input received
        Displays error messages for invalid input
    
    Example:
        >>> get_numeric_input("Enter a number: ")
        Enter a number: abc
        Invalid number entered. Please enter a numeric value.
        Enter a number: 42.5
        42.5
    """
```

**Preconditions**: prompt is a non-empty string  
**Postconditions**: Returns valid float  
**Behavior**: Loops until valid input, displays errors inline

---

### Function: execute_operation

```python
def execute_operation(operation_choice: int) -> None:
    """
    Execute the selected calculator operation.
    
    Args:
        operation_choice: Menu choice number (1-8)
    
    Returns:
        None (displays result to stdout)
    
    Side Effects:
        - Prompts user for operands
        - Performs calculation
        - Displays result or error message
    
    Behavior:
        1. Prompt for operand(s) based on operation type
        2. Validate inputs
        3. Call appropriate operation function
        4. Display result
        5. Handle any errors gracefully
    """
```

**Preconditions**: operation_choice is valid menu option (1-8)  
**Postconditions**: Result or error message displayed  
**Side Effects**: User interaction, console output

---

### Function: main

```python
def main() -> None:
    """
    Main entry point for the calculator application.
    
    Runs the calculator main loop:
    1. Display menu
    2. Get user choice
    3. Execute operation or exit
    4. Repeat
    
    Returns:
        None
    
    Side Effects:
        - Runs until user selects exit
        - All user interaction
        - Catches KeyboardInterrupt (Ctrl+C) gracefully
    """
```

**Preconditions**: None  
**Postconditions**: Application exits cleanly  
**Behavior**: Infinite loop until exit, handles Ctrl+C gracefully

---

## Error Handling Contract

All modules follow consistent error handling:

**Operations Module**:
- Invalid operations raise ValueError with descriptive message
- No silent failures
- No returning None or special values for errors

**Validators Module**:
- Never raise exceptions
- Always return (bool, str) tuple
- Clear, user-friendly error messages

**Calculator Module**:
- Catches all exceptions from operations
- Displays user-friendly error messages
- Never exposes stack traces to user
- Continues operation after errors

---

## Testing Contract

All functions must have tests covering:

1. **Normal cases**: Expected inputs and outputs
2. **Edge cases**: Boundaries (0, negative, very large)
3. **Error cases**: Invalid inputs, error conditions
4. **Coverage**: 90%+ code coverage required

---

## Performance Contract

All operations must meet:

- **Calculation time**: <1ms per operation
- **Total response time**: <100ms (excluding user input time)
- **Memory usage**: <10MB total
- **Session stability**: 100+ consecutive operations without degradation

---

## Summary

This contract specification defines all public interfaces for the Calculator application. All modules must adhere to these contracts to ensure correctness, maintainability, and constitutional compliance.
