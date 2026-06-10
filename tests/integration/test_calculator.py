"""
Integration tests for Calculator CLI application.

Tests the complete workflow from menu display through operation execution.
Uses input/output mocking to simulate user interaction.
"""

import pytest
from io import StringIO
from unittest.mock import patch
from src.calculator import display_menu, get_menu_choice, get_numeric_input, execute_operation, main


class TestCalculatorWorkflow:
    """Integration tests for complete calculation workflows."""

    def test_complete_calculation_workflow(self):
        """Test a complete calculation from menu to result."""
        # This test will verify the full workflow once implemented
        # For now, we'll test individual components
        pass

    def test_multiple_consecutive_calculations(self):
        """Test multiple calculations in one session."""
        # Test that the calculator can handle multiple operations
        # without crashing or losing state
        pass

    def test_clean_exit_via_menu(self):
        """Test clean exit when user selects exit option."""
        # Verify that choosing exit option (0) terminates gracefully
        pass


class TestMenuDisplay:
    """Test menu display functionality."""

    def test_display_menu_shows_all_options(self, capsys):
        """Test that menu displays all 8 operations plus exit."""
        display_menu()
        captured = capsys.readouterr()
        output = captured.out

        # Check that all operations are displayed
        assert "1" in output and "Addition" in output
        assert "2" in output and "Subtraction" in output
        assert "3" in output and "Multiplication" in output
        assert "4" in output and "Division" in output
        assert "5" in output and "Power" in output
        assert "6" in output and "Square Root" in output
        assert "7" in output and "Percentage" in output
        assert "8" in output and "Modulus" in output
        assert "0" in output and "Exit" in output


class TestInputHandling:
    """Test input handling and validation."""

    @patch('builtins.input', return_value='1')
    def test_get_menu_choice_valid(self, mock_input):
        """Test getting valid menu choice."""
        choice = get_menu_choice()
        assert choice == 1

    @patch('builtins.input', side_effect=['invalid', '1'])
    def test_get_menu_choice_retry_on_invalid(self, mock_input):
        """Test that invalid menu choice prompts retry."""
        choice = get_menu_choice()
        assert choice == 1
        assert mock_input.call_count == 2

    @patch('builtins.input', return_value='42.5')
    def test_get_numeric_input_valid(self, mock_input):
        """Test getting valid numeric input."""
        number = get_numeric_input("Enter a number: ")
        assert number == 42.5

    @patch('builtins.input', side_effect=['abc', '10.5'])
    def test_get_numeric_input_retry_on_invalid(self, mock_input):
        """Test that invalid numeric input prompts retry."""
        number = get_numeric_input("Enter a number: ")
        assert number == 10.5
        assert mock_input.call_count == 2
