import pytest
from src.api.logic.expression_evaluator import ExpressionEvaluator


class TestSafeEvaluator:
    """Tests for the SafeEvaluator class functionality."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.evaluator = ExpressionEvaluator()

    @pytest.mark.parametrize(
        "expression, expected_result",
        [
            # Additional valid expressions
            ("1 - -1", 2),
            ("(3 + 2) * 2", 10),  # Use of parentheses
            ("3 + (2 * 2)", 7),  # Order of operations
            ("2 + 3 * 5", 17),  # Multiplication before addition
            ("18 / (2 * 3)", 3),  # Division and parentheses
            # Divisions
            ("10 / 2 / 5", 1),
            ("100 / (5 * 5)", 4),
            # Nested parentheses
            ("((2 + 3) * 5)", 25),
            ("(2 + (3 * 5))", 17),
            # Unary operations
            ("-(-3)", 3),
            # Zero and negative combinations
            ("0 * -1", 0),
            ("-1 * 0", 0),
            ("0 / -1", 0),
            ("-1 / 1", -1),
            # Floats
            ("3.5 * 2", 7.0),
            ("4 + 2.5", 6.5),
            # Complex expression
            ("2 * (3 + 5) - 4 / 2 + 10", 24),
            ("2 + 2 * 2", 6),
        ],
    )
    def test_evaluate_valid_expression(self, expression, expected_result):
        """Tests the evaluation of valid arithmetic expressions."""
        assert self.evaluator.evaluate(expression) == expected_result

    @pytest.mark.parametrize(
        "expression, error_type",
        [
            ("2 / 0", ZeroDivisionError),  # Division by zero
            ("two + three", NameError),  # Non-numeric values
            ("3 **", SyntaxError),  # Incomplete expression
            ("3 +* 4", SyntaxError),  # Invalid operator combination
            ("(3 + 2", SyntaxError),  # Mismatched parentheses
            ("3 3 + 2", SyntaxError),  # Missing operator
            ("", SyntaxError),  # Empty string
        ],
    )
    def test_evaluate_invalid_expression(self, expression, error_type):
        """Tests the evaluation of invalid arithmetic expressions."""
        with pytest.raises(error_type):
            self.evaluator.evaluate(expression)
