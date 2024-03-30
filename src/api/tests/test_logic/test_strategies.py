import pytest
from src.api.logic.strategies import (
    AdditionStrategy,
    SubtractionStrategy,
    MultiplicationStrategy,
    DivisionStrategy,
)


class TestAdditionStrategy:
    """Tests the behavior of the addition operation strategy."""

    def setup_method(self):
        self.strategy = AdditionStrategy()

    @pytest.mark.parametrize(
        "operand1, operand2, expected_result",
        [
            (1, 2, 3),
            (-1, -2, -3),
            (0, 0, 0),
        ],
    )
    def test_execute(self, operand1, operand2, expected_result):
        """Ensures addition of operands yields the correct result."""
        assert self.strategy.execute(operand1, operand2) == expected_result


class TestSubtractionStrategy:
    """Tests the behavior of the subtraction operation strategy."""

    def setup_method(self):
        self.strategy = SubtractionStrategy()

    @pytest.mark.parametrize(
        "operand1, operand2, expected_result",
        [
            (3, 2, 1),
            (-1, -2, 1),
            (0, 0, 0),
        ],
    )
    def test_execute(self, operand1, operand2, expected_result):
        """Ensures subtraction of operands yields the correct result."""
        assert self.strategy.execute(operand1, operand2) == expected_result


class TestMultiplicationStrategy:
    """Tests the behavior of the multiplication operation strategy."""

    def setup_method(self):
        self.strategy = MultiplicationStrategy()

    @pytest.mark.parametrize(
        "operand1, operand2, expected_result",
        [
            (3, 2, 6),
            (-1, -2, 2),
            (0, 5, 0),
        ],
    )
    def test_execute(self, operand1, operand2, expected_result):
        """Ensures multiplication of operands yields the correct result."""
        assert self.strategy.execute(operand1, operand2) == expected_result


class TestDivisionStrategy:
    """Tests the behavior of the division operation strategy."""

    def setup_method(self):
        """Initializes the DivisionStrategy instance before each test method."""
        self.strategy = DivisionStrategy()

    @pytest.mark.parametrize(
        "operand1, operand2, expected_result",
        [
            (6, 2, 3),
            (-4, -2, 2),
            (0, 5, 0),
        ],
    )
    def test_execute(self, operand1, operand2, expected_result):
        """Ensures division of operands yields the correct result, except when dividing by zero."""
        assert self.strategy.execute(operand1, operand2) == expected_result

    def test_division_by_zero(self):
        """Verifies that attempting to divide by zero raises a ValueError."""
        with pytest.raises(ZeroDivisionError):
            self.strategy.execute(1, 0)
