# Calculator

A modern command-line calculator application built in Python with **Rich terminal UI** that performs accurate mathematical calculations with comprehensive input validation and error handling.

## Features

### Core Arithmetic Operations
- **Addition**: Add two numbers
- **Subtraction**: Subtract one number from another
- **Multiplication**: Multiply two numbers
- **Division**: Divide with automatic zero-division protection

### Extended Mathematical Operations
- **Power**: Raise a number to any exponent
- **Square Root**: Calculate square roots with negative number protection
- **Percentage**: Calculate percentage of a value
- **Modulus**: Find remainder of division

### User Experience
- **Rich Terminal UI**: Beautiful colored interface with formatted menus and results
- **Menu-based interface**: No complex expression parsing needed
- **Comprehensive input validation**: Prevents invalid input with clear error messages
- **Visual feedback**: Color-coded results (green for success, red for errors)
- **Multiple calculations per session**: Continuous operation without restart
- **Clean exit option**: Graceful shutdown

## Requirements

- Python 3.8 or higher
- Rich 13.0.0+ (for terminal UI)
- pytest 7.0.0+ (for testing)
- pytest-cov 4.0.0+ (for coverage reports)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd calcu
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the calculator from the command line:

```bash
python -m src.calculator
```

### Example Session

```
╭─────────────── Welcome to Calculator ───────────────╮
│  A modern command-line calculator with Rich UI      │
│         Perform accurate calculations with style     │
╰──────────────────────────────────────────────────────╯

╭───────────── Calculator Menu ─────────────╮
│  1        Addition                         │
│  2        Subtraction                      │
│  3        Multiplication                   │
│  4        Division                         │
│  5        Power                            │
│  6        Square Root                      │
│  7        Percentage                       │
│  8        Modulus                          │
│                                            │
│  0        Exit                             │
╰────────────────────────────────────────────╯

Enter your choice (0-8): 1
Enter first number: 42
Enter second number: 8

✓ Result: 42.0 + 8.0 = 50.0

[Menu displays again for next calculation...]
```

*Note: Actual output includes colors - green for results, red for errors, cyan for menus*
8. Modulus
0. Exit
==================================================

Enter your choice (0-8): 1
Enter first number: 42
Enter second number: 8

Result: 42.0 + 8.0 = 50.0

[Menu displays again...]
```

### Operation Examples

**Addition**: Add two numbers
```
Choice: 1
Enter first number: 15
Enter second number: 27
Result: 15.0 + 27.0 = 42.0
```

**Division**: Divide with error handling
```
Choice: 4
Enter first number: 10
Enter second number: 0
Error: Cannot divide by zero
```

**Square Root**: Calculate square root
```
Choice: 6
Enter number: 16
Result: √16.0 = 4.0
```

**Percentage**: Calculate percentage of a value
```
Choice: 7
Enter percentage: 20
Enter value: 150
Result: 20.0% of 150.0 = 30.0
```

## Testing

Run the complete test suite:

```bash
# Run all tests
pytest -v

# Run with coverage report
pytest --cov=src --cov-report=term-missing

# Run specific test file
pytest tests/unit/test_operations.py -v
```

### Test Coverage

The project maintains >90% test coverage as per project requirements:
- Unit tests for all mathematical operations
- Unit tests for all input validation functions
- Integration tests for complete user workflows

## Project Structure

```
calcu/
├── src/
│   ├── __init__.py
│   ├── operations.py       # Mathematical operations
│   ├── validators.py       # Input validation
│   └── calculator.py       # Main CLI application
├── tests/
│   ├── __init__.py
│   ├── unit/
│   │   ├── test_operations.py
│   │   └── test_validators.py
│   └── integration/
│       └── test_calculator.py
├── requirements.txt
└── README.md
```

## Architecture

The calculator follows a modular architecture with strict separation of concerns:

- **operations.py**: Pure mathematical functions with no side effects
- **validators.py**: Input validation and error detection
- **calculator.py**: User interface, menu system, and session management

This design ensures:
- Easy testing (pure functions)
- Easy maintenance (clear module boundaries)
- Easy extension (add new operations without modifying existing code)
- Security (no eval() or exec(), explicit input validation)

## Error Handling

The calculator handles common error scenarios gracefully:

- **Division by zero**: Displays error message, continues running
- **Negative square root**: Displays error message, continues running
- **Invalid input**: Prompts user to re-enter valid data
- **Invalid menu choice**: Prompts user to select valid option
- **Keyboard interrupt (Ctrl+C)**: Exits cleanly with goodbye message

## Development

### Code Quality Standards

- PEP 8 compliance for Python code style
- Type hints for all function signatures
- Google-style docstrings for all public functions
- Comprehensive test coverage (>90%)
- No external dependencies beyond testing tools

### Adding New Operations

To add a new operation:

1. Add the operation function to `src/operations.py`:
```python
def new_operation(a: float, b: float) -> float:
    """Docstring here."""
    return result
```

2. Add test cases to `tests/unit/test_operations.py`

3. Add menu option to `display_menu()` in `src/calculator.py`

4. Add elif branch to `execute_operation()` in `src/calculator.py`

5. Update `validate_menu_choice()` range in `src/validators.py`

## License

[Add license information]

## Contributing

[Add contribution guidelines]

## Support

For issues or questions, please [add contact information or issue tracker link].
