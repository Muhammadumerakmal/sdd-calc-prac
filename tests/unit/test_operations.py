"""
Unit tests for mathematical operations.

Tests all operations in src/operations.py following the Red-Green-Refactor TDD approach.
Each test function tests one specific scenario with descriptive names.
"""

import pytest
from src.operations import add, subtract, multiply, divide, power, square_root, percentage, modulus


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


class TestPower:
    """Test cases for the power function."""

    def test_power_positive_exponent(self):
        """Test power with positive exponent."""
        assert power(2.0, 8.0) == 256.0
        assert power(10.0, 3.0) == 1000.0
        assert power(5.0, 2.0) == 25.0

    def test_power_zero_exponent(self):
        """Test power with zero exponent."""
        assert power(5.0, 0.0) == 1.0
        assert power(100.0, 0.0) == 1.0
        assert power(0.0, 0.0) == 1.0

    def test_power_negative_exponent(self):
        """Test power with negative exponent."""
        assert power(2.0, -1.0) == 0.5
        assert power(10.0, -2.0) == 0.01


class TestSquareRoot:
    """Test cases for the square_root function."""

    def test_square_root_positive(self):
        """Test square root of positive numbers."""
        assert square_root(16.0) == 4.0
        assert square_root(25.0) == 5.0
        assert square_root(2.0) == pytest.approx(1.4142135623730951)

    def test_square_root_zero(self):
        """Test square root of zero."""
        assert square_root(0.0) == 0.0

    def test_square_root_negative_raises_error(self):
        """Test that square root of negative raises ValueError."""
        with pytest.raises(ValueError, match="non-negative"):
            square_root(-9.0)
        with pytest.raises(ValueError, match="non-negative"):
            square_root(-1.0)


class TestPercentage:
    """Test cases for the percentage function."""

    def test_percentage_basic(self):
        """Test basic percentage calculations."""
        assert percentage(20.0, 50.0) == 10.0
        assert percentage(50.0, 100.0) == 50.0
        assert percentage(100.0, 25.0) == 25.0

    def test_percentage_zero(self):
        """Test percentage with zero."""
        assert percentage(0.0, 100.0) == 0.0
        assert percentage(50.0, 0.0) == 0.0


class TestModulus:
    """Test cases for the modulus function."""

    def test_modulus_basic(self):
        """Test basic modulus operations."""
        assert modulus(17.0, 5.0) == 2.0
        assert modulus(10.0, 3.0) == 1.0
        assert modulus(8.0, 4.0) == 0.0

    def test_modulus_zero_divisor_raises_error(self):
        """Test that modulus by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            modulus(10.0, 0.0)
