"""
Unit tests for mathematical operations.

Tests all operations in src/operations.py following the Red-Green-Refactor TDD approach.
Each test function tests one specific scenario with descriptive names.
"""

import pytest
from src.operations import add, subtract, multiply, divide


class TestAddition:
    """Test cases for the add function."""

    def test_add_positive_numbers(self):
        """Test addition of two positive numbers."""
        assert add(2.0, 3.0) == 5.0
        assert add(10.0, 25.0) == 35.0

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        assert add(-5.0, -3.0) == -8.0
        assert add(-10.0, 5.0) == -5.0
        assert add(10.0, -5.0) == 5.0

    def test_add_zero(self):
        """Test addition with zero."""
        assert add(0.0, 0.0) == 0.0
        assert add(5.0, 0.0) == 5.0
        assert add(0.0, 10.0) == 10.0


class TestSubtraction:
    """Test cases for the subtract function."""

    def test_subtract_positive(self):
        """Test subtraction of positive numbers."""
        assert subtract(10.0, 3.0) == 7.0
        assert subtract(25.0, 10.0) == 15.0

    def test_subtract_negative(self):
        """Test subtraction with negative numbers."""
        assert subtract(-5.0, -3.0) == -2.0
        assert subtract(-10.0, 5.0) == -15.0
        assert subtract(10.0, -5.0) == 15.0

    def test_subtract_result_negative(self):
        """Test subtraction resulting in negative number."""
        assert subtract(5.0, 10.0) == -5.0
        assert subtract(0.0, 10.0) == -10.0


class TestMultiplication:
    """Test cases for the multiply function."""

    def test_multiply_positive(self):
        """Test multiplication of positive numbers."""
        assert multiply(6.0, 7.0) == 42.0
        assert multiply(4.0, 5.0) == 20.0

    def test_multiply_negative(self):
        """Test multiplication with negative numbers."""
        assert multiply(-5.0, 3.0) == -15.0
        assert multiply(-4.0, -3.0) == 12.0
        assert multiply(7.0, -2.0) == -14.0

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        assert multiply(0.0, 100.0) == 0.0
        assert multiply(100.0, 0.0) == 0.0
        assert multiply(0.0, 0.0) == 0.0


class TestDivision:
    """Test cases for the divide function."""

    def test_divide_positive(self):
        """Test division of positive numbers."""
        assert divide(15.0, 3.0) == 5.0
        assert divide(20.0, 4.0) == 5.0

    def test_divide_result_decimal(self):
        """Test division resulting in decimal."""
        assert divide(7.0, 2.0) == 3.5
        assert divide(10.0, 4.0) == 2.5

    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10.0, 0.0)
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(0.0, 0.0)
