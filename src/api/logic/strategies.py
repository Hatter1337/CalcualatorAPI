import ast
from abc import ABC, abstractmethod
from functools import update_wrapper


class OperationRegistry:
    """Registry for operation strategies."""

    registry = {}

    @classmethod
    def register(cls, op_type):
        """
        Decorator to register a strategy class for a specific operation type.

        Args:
            op_type: The operation type to register the strategy for.

        Returns:
            A decorator function that registers the provided strategy class.
        """

        def decorator(strategy_cls):
            # Initialize the class to store in the registry
            instance = strategy_cls()
            # Use update_wrapper to copy metadata from the class to the instance
            update_wrapper(instance, strategy_cls, updated=())
            # Register the instance with its metadata
            cls.registry[op_type] = instance
            return strategy_cls

        return decorator

    @classmethod
    def get_strategy(cls, op_type):
        """
        Retrieves a registered strategy class for a given operation type.

        Args:
            op_type: The operation type to retrieve the strategy for.

        Returns:
            The registered strategy class instance, or None if not registered.
        """
        return cls.registry.get(op_type)


class CalculationStrategy(ABC):
    @abstractmethod
    def execute(self, operand1: float, operand2: float) -> float:
        """
        Execute a mathematical operation on two operands.

        Args:
            operand1 (float): The first operand in the operation.
            operand2 (float): The second operand in the operation.

        Returns:
            float: The result of the operation.
        """


@OperationRegistry.register(ast.Add)
class AdditionStrategy(CalculationStrategy):
    def execute(self, operand1: float, operand2: float) -> float:
        """Performs addition of two operands."""
        return operand1 + operand2


@OperationRegistry.register(ast.Sub)
class SubtractionStrategy(CalculationStrategy):
    def execute(self, operand1: float, operand2: float) -> float:
        """Performs subtraction of two operands."""
        return operand1 - operand2


@OperationRegistry.register(ast.Mult)
class MultiplicationStrategy(CalculationStrategy):
    def execute(self, operand1: float, operand2: float) -> float:
        """Performs multiplication of two operands."""
        return operand1 * operand2


@OperationRegistry.register(ast.Div)
class DivisionStrategy(CalculationStrategy):
    def execute(self, operand1: float, operand2: float) -> float:
        """Performs division of two operands.

        Raises:
            ValueError: If the second operand is zero.
        """
        if operand2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return operand1 / operand2
