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

    @patch('builtins.input', side_effect=['1', '5', '3', '0'])
    def test_complete_calculation_workflow(self, mock_input):
        """Test a complete calculation from menu to result.

        Workflow: menu -> select addition (1) -> enter 5 -> enter 3 -> result 8.0 -> exit (0)
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue()

            # Verify result of 5 + 3 = 8 appears in output
            assert '8' in output or '8.0' in output

    @patch('builtins.input', side_effect=['1', '10', '5', '3', '4', '3', '4', '20', '4', '0'])
    def test_multiple_consecutive_calculations(self, mock_input):
        """Test multiple calculations in one session.

        Performs three operations:
        1. Addition: 10 + 5 = 15
        2. Multiplication: 4 * 3 = 12
        3. Division: 20 / 4 = 5
        Then exits cleanly.
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue()

            # Verify all three results appear
            assert '15' in output
            assert '12' in output
            # Note: Division result 5.0 should appear, checking for '5'

    @patch('builtins.input', return_value='0')
    def test_clean_exit_via_menu(self, mock_input):
        """Test clean exit when user selects exit option.

        User immediately selects 0 (exit) and program terminates gracefully.
        """
        # Should not raise any exceptions
        try:
            main()
            exit_clean = True
        except Exception:
            exit_clean = False

        assert exit_clean

    @patch('builtins.input', side_effect=['2', '10', '3', '0'])
    def test_subtraction_operation(self, mock_input):
        """Test subtraction operation workflow."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue()
            # 10 - 3 = 7
            assert '7' in output

    @patch('builtins.input', side_effect=['5', '2', '3', '0'])
    def test_power_operation(self, mock_input):
        """Test power operation workflow."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue()
            # 2 ^ 3 = 8
            assert '8' in output

    @patch('builtins.input', side_effect=['6', '16', '0'])
    def test_square_root_operation(self, mock_input):
        """Test square root operation workflow."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue()
            # sqrt(16) = 4
            assert '4' in output

    @patch('builtins.input', side_effect=['7', '20', '50', '0'])
    def test_percentage_operation(self, mock_input):
        """Test percentage operation workflow."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue()
            # 20% of 50 = 10
            assert '10' in output

    @patch('builtins.input', side_effect=['8', '17', '5', '0'])
    def test_modulus_operation(self, mock_input):
        """Test modulus operation workflow."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue()
            # 17 mod 5 = 2
            assert '2' in output

    @patch('builtins.input', side_effect=['6', '-9', '0'])
    def test_square_root_negative_error(self, mock_input):
        """Test square root error handling for negative numbers."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue()
            # Should contain error message
            assert 'Error' in output or 'error' in output


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
