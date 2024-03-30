import ast
from .strategies import OperationRegistry


class ExpressionEvaluator:
    """Evaluates mathematical expressions using registered operation strategies."""

    def __init__(self):
        """Initializes the evaluator with available operation strategies."""
        self.allowed_methods = OperationRegistry.registry

    def evaluate(self, expression):
        """
        Evaluates a mathematical expression.

        Args:
            expression (str): The expression to evaluate.

        Returns:
            The result of the evaluation or an error message.
        """
        try:
            parsed_expr = ast.parse(expression, mode="eval")
            return self._eval(parsed_expr.body)
        except (ZeroDivisionError, NameError, SyntaxError):
            raise
        except Exception as e:
            return f"Error: {str(e)}"

    def _eval(self, node):
        """
        Recursively evaluates an AST node.

        Args:
            node (ast.AST, ast.BinOp): The AST node to evaluate.

        Returns:
            The evaluation result of the node.

        Raises:
            ValueError: If an unsupported operation or disallowed name is used.
            TypeError: If the expression contains an unsupported type.
        """
        if isinstance(node, ast.Num):  # for Python versions < 3.8
            return node.n
        elif isinstance(node, ast.Constant):  # for Python versions >= 3.8
            return node.value
        elif isinstance(node, ast.BinOp):
            left = self._eval(node.left)
            right = self._eval(node.right)

            op_type = type(node.op)
            strategy_cls = self.allowed_methods.get(op_type)

            if strategy_cls:
                return strategy_cls.execute(left, right)
            else:
                raise ValueError("Unsupported operation")
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            operand = self._eval(node.operand)
            return -operand  # Handle unary negation
        elif isinstance(node, ast.Name):
            if node.id in self.allowed_methods:
                return self.allowed_methods[node.id]
            else:
                raise NameError(f"Use of disallowed name: {node.id}")
        else:
            raise TypeError("Unsupported expression type")
