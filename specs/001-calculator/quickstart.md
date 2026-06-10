# Calculator Quickstart Guide

**Version**: 1.0  
**Last Updated**: 2026-06-10

## Overview

Calculator is a command-line application that performs mathematical calculations including core arithmetic (addition, subtraction, multiplication, division) and extended operations (power, square root, percentage, modulus).

## Requirements

- **Python**: 3.8 or higher
- **Operating System**: Windows, macOS, or Linux
- **Dependencies**: None (uses Python standard library only)

## Installation

### Step 1: Clone or Download

```bash
# If using Git
git clone <repository-url>
cd calcu

# Or download and extract the ZIP file
```

### Step 2: Verify Python Version

```bash
python --version
# Should show Python 3.8.x or higher
```

### Step 3: Install Development Dependencies (Optional)

Only needed if running tests:

```bash
pip install -r requirements.txt
# Installs pytest and pytest-cov for testing
```

## Running the Calculator

### Basic Usage

```bash
python src/calculator.py
```

You'll see the calculator menu:

```
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
```

### Example Session

```
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

Select an operation (0-8): 1

Enter first number: 5
Enter second number: 3

Result: 8.0

[Menu displays again for next calculation]
```

## Operations Guide

### 1. Addition

**Menu Option**: 1

**Description**: Adds two numbers

**Example**:
```
Select: 1
First number: 10
Second number: 25
Result: 35.0
```

### 2. Subtraction

**Menu Option**: 2

**Description**: Subtracts the second number from the first

**Example**:
```
Select: 2
First number: 50
Second number: 15
Result: 35.0
```

### 3. Multiplication

**Menu Option**: 3

**Description**: Multiplies two numbers

**Example**:
```
Select: 3
First number: 6
Second number: 7
Result: 42.0
```

### 4. Division

**Menu Option**: 4

**Description**: Divides the first number by the second

**Example**:
```
Select: 4
First number: 20
Second number: 4
Result: 5.0
```

**Note**: Division by zero is prevented with an error message.

### 5. Power

**Menu Option**: 5

**Description**: Raises the first number (base) to the power of the second number (exponent)

**Example**:
```
Select: 5
Enter base: 2
Enter exponent: 8
Result: 256.0
```

### 6. Square Root

**Menu Option**: 6

**Description**: Calculates the square root of a number

**Example**:
```
Select: 6
Enter number: 16
Result: 4.0
```

**Note**: Square root of negative numbers is not allowed and will show an error message.

### 7. Percentage

**Menu Option**: 7

**Description**: Calculates a percentage of a value (e.g., 20% of 50)

**Example**:
```
Select: 7
Enter percentage: 20
Enter value: 50
Result: 10.0
```

### 8. Modulus

**Menu Option**: 8

**Description**: Calculates the remainder of division

**Example**:
```
Select: 8
First number: 17
Second number: 5
Result: 2.0
```

## Error Handling

The calculator handles errors gracefully and continues running:

### Invalid Number Input

```
Enter first number: abc
Invalid number entered. Please enter a numeric value.
Enter first number: 42
[Continues normally]
```

### Division by Zero

```
Select: 4
First number: 10
Second number: 0
Cannot divide by zero.
[Returns to menu]
```

### Negative Square Root

```
Select: 6
Enter number: -9
Square root requires a non-negative number.
[Returns to menu]
```

### Invalid Menu Choice

```
Select an operation (0-8): 99
Invalid menu choice. Please select a number from 0-8.
[Prompts again]
```

## Exiting the Calculator

Select option `0` from the menu:

```
Select an operation (0-8): 0
Thank you for using Calculator. Goodbye!
```

Or press `Ctrl+C` at any time to exit immediately.

## Tips and Tricks

### Decimal Numbers

The calculator supports decimal numbers:

```
First number: 3.14
Second number: 2.5
```

### Negative Numbers

Enter negative numbers with a minus sign:

```
First number: -10
Second number: 5
Result: -5.0
```

### Large Numbers

The calculator handles very large numbers within Python's float range (up to ±10^308):

```
First number: 1000000
Second number: 1000000
Result: 1000000000000.0
```

### Multiple Calculations

Perform as many calculations as needed in a single session—the menu returns after each calculation.

## Running Tests

If you've installed development dependencies:

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src --cov-report=term-missing

# Run specific test file
pytest tests/unit/test_operations.py
```

Expected output:
```
================================ test session starts =================================
collected 45 items

tests/unit/test_operations.py ...................... [ 48%]
tests/unit/test_validators.py .................... [ 88%]
tests/integration/test_calculator.py ..... [100%]

================================ 45 passed in 0.23s ==================================
```

## Troubleshooting

### "Python not found"

Ensure Python 3.8+ is installed and in your PATH:

```bash
# Windows
py --version

# macOS/Linux
python3 --version
```

### "Module not found" Error

Ensure you're running from the project root directory:

```bash
pwd  # Should show .../calcu
ls   # Should show src/ directory
```

### Calculator Won't Start

Check that the file has execute permissions (macOS/Linux):

```bash
chmod +x src/calculator.py
```

## Support and Documentation

- **Full Documentation**: See `README.md` in project root
- **Constitution**: See `.specify/memory/constitution.md` for project principles
- **Specification**: See `specs/001-calculator/spec.md` for requirements
- **Implementation Plan**: See `specs/001-calculator/plan.md` for architecture

## Quick Reference

| Operation | Menu Option | Format |
|-----------|-------------|--------|
| Addition | 1 | a + b |
| Subtraction | 2 | a - b |
| Multiplication | 3 | a × b |
| Division | 4 | a ÷ b |
| Power | 5 | a ^ b |
| Square Root | 6 | √a |
| Percentage | 7 | a% of b |
| Modulus | 8 | a mod b |
| Exit | 0 | - |

---

**Ready to calculate?** Run `python src/calculator.py` to get started!
