# Data Model: Calculator

**Feature**: Calculator  
**Date**: 2026-06-10  
**Status**: Complete

## Overview

This document defines the data structures and entities used in the Calculator application. Since this is a stateless command-line calculator with no persistence, the data model focuses on runtime entities and validation structures.

## Core Entities

### 1. Operation

**Description**: Represents a mathematical operation requested by the user.

**Attributes**:
- `operation_type` (OperationType): The type of mathematical operation
- `operand_a` (float): The first operand (required for all operations)
- `operand_b` (float | None): The second operand (required for binary operations, None for unary)
- `result` (float | None): The calculated result (None before calculation)
- `error` (str | None): Error message if operation failed (None on success)

**Valid States**:
- **Pending**: operation_type and operand(s) set, result is None, error is None
- **Success**: result is set, error is None
- **Failed**: result is None, error message is set

**State Transitions**:
```
[User Input] → Pending → [Calculate] → Success
                       ↘ [Error] → Failed
```

**Example Instances**:
```python
# Success case
Operation(
    operation_type=OperationType.ADD,
    operand_a=5.0,
    operand_b=3.0,
    result=8.0,
    error=None
)

# Error case
Operation(
    operation_type=OperationType.DIVIDE,
    operand_a=10.0,
    operand_b=0.0,
    result=None,
    error="Cannot divide by zero"
)
```

---

### 2. OperationType (Enum)

**Description**: Enumeration of supported mathematical operations.

**Values**:
- `ADD`: Addition (a + b)
- `SUBTRACT`: Subtraction (a - b)
- `MULTIPLY`: Multiplication (a * b)
- `DIVIDE`: Division (a / b)
- `POWER`: Exponentiation (a ^ b)
- `SQUARE_ROOT`: Square root (√a)
- `PERCENTAGE`: Percentage calculation (a% of b)
- `MODULUS`: Modulus/remainder (a mod b)

**Binary Operations** (require two operands):
- ADD, SUBTRACT, MULTIPLY, DIVIDE, POWER, PERCENTAGE, MODULUS

**Unary Operations** (require one operand):
- SQUARE_ROOT

**Validation Rules**:
- DIVIDE: operand_b must not be zero
- SQUARE_ROOT: operand_a must be non-negative
- All operations: operands must be valid float values

---

### 3. ValidationResult

**Description**: Represents the outcome of input validation.

**Attributes**:
- `is_valid` (bool): Whether the input passed validation
- `error_message` (str): Human-readable error message (empty string if valid)
- `parsed_value` (float | int | None): The successfully parsed value (None if invalid)

**Example Instances**:
```python
# Valid input
ValidationResult(
    is_valid=True,
    error_message="",
    parsed_value=42.5
)

# Invalid input
ValidationResult(
    is_valid=False,
    error_message="Invalid number entered. Please enter a numeric value.",
    parsed_value=None
)
```

---

### 4. MenuChoice

**Description**: Represents a user's menu selection.

**Attributes**:
- `choice_id` (int): The numeric menu option selected
- `operation_type` (OperationType | None): The corresponding operation (None for exit)
- `is_exit` (bool): Whether this choice exits the application

**Valid Menu Choices**:
```
1 → ADD
2 → SUBTRACT
3 → MULTIPLY
4 → DIVIDE
5 → POWER
6 → SQUARE_ROOT
7 → PERCENTAGE
8 → MODULUS
0 → EXIT
```

---

### 5. Session

**Description**: Represents a user's calculator session (runtime only, not persisted).

**Attributes**:
- `is_active` (bool): Whether the session is still running
- `operation_count` (int): Number of operations performed this session
- `last_result` (float | None): Result of the most recent calculation

**State**:
- Session state is implicit in the main loop's while condition
- No formal Session object implemented (kept simple per constitutional requirements)
- Session "ends" when user selects exit option or terminates process

---

## Data Flow

### User Input → Validation → Operation → Result

```
1. User Input (string)
   ↓
2. Validation (ValidationResult)
   ↓ (if valid)
3. Parse to float
   ↓
4. Create Operation
   ↓
5. Execute calculation
   ↓
6. Operation with result or error
   ↓
7. Display to user
```

### Validation Rules by Input Type

**Numeric Input Validation**:
- Must be convertible to float
- Can be negative (e.g., "-5")
- Can be decimal (e.g., "3.14")
- Cannot be empty string
- Cannot contain letters or special characters (except decimal point and leading minus)

**Menu Choice Validation**:
- Must be convertible to integer
- Must be in range [0, 8]
- 0 is reserved for exit

**Operation-Specific Validation**:
- Division: operand_b ≠ 0
- Square root: operand_a ≥ 0
- All operations: operands must be within float range

---

## Error Messages

**Standardized Error Messages** (for consistency):

| Error Type | Message |
|------------|---------|
| Non-numeric input | "Invalid number entered. Please enter a numeric value." |
| Empty input | "Input cannot be empty. Please enter a value." |
| Invalid menu choice | "Invalid menu choice. Please select a number from 0-8." |
| Division by zero | "Cannot divide by zero." |
| Negative square root | "Square root requires a non-negative number." |
| Overflow | "Number too large to calculate." |
| Generic error | "An error occurred. Please try again." |

---

## Type Definitions (Python)

```python
from enum import Enum
from typing import Optional, Tuple

class OperationType(Enum):
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"
    POWER = "power"
    SQUARE_ROOT = "square_root"
    PERCENTAGE = "percentage"
    MODULUS = "modulus"

# Validation result type
ValidationResult = Tuple[bool, str]  # (is_valid, error_message)

# Operation result type
OperationResult = float  # or raises ValueError

# Menu choice type
MenuChoice = int  # 0-8
```

---

## Relationships

**No persistent relationships** (stateless application):
- Operations are independent
- No history tracking
- No user accounts
- No operation chaining (each calculation is atomic)

**Runtime relationships**:
- MenuChoice → OperationType (mapping)
- OperationType → Operation function (dispatch)
- Operation function → ValidationResult (input validation)
- Operation → float result (output)

---

## Constraints

### Data Constraints
- **Float range**: ±1.7976931348623157e+308 (Python float max)
- **Precision**: ~15-17 significant decimal digits
- **Display precision**: Up to 10 decimal places, trailing zeros stripped

### Business Constraints
- One operation per interaction cycle
- No operation history retention
- No intermediate results storage (except displayed to user)
- Session state not persisted between program runs

---

## Extension Points

For future enhancements, the data model can be extended without breaking existing code:

**Future Entity: CalculationHistory**
- Would store sequence of operations
- Attributes: operations[], timestamps[], session_id
- Currently out of scope per spec

**Future Entity: UserPreferences**
- Would store decimal precision preference, display format
- Currently out of scope per spec

**Future OperationTypes**:
- SINE, COSINE, TANGENT (trigonometric)
- LOG, LN (logarithmic)
- FACTORIAL, COMBINATIONS (combinatorics)
- Architecture supports adding via enum extension

---

## Summary

The Calculator data model is intentionally minimal, focusing on runtime validation and operation execution. No persistence layer is needed, keeping the architecture simple per constitutional requirements. All entities are well-defined with clear validation rules and error handling strategies.
