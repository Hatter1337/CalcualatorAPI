import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from logic.expression_evaluator import ExpressionEvaluator


app = FastAPI()
logger = logging.getLogger("uvicorn")
expression_evaluator = ExpressionEvaluator()


class CalculatorInput(BaseModel):
    """Input for expression calculation."""

    expression: str


@app.post("/calculate")
def calculate_expression(c_input: CalculatorInput):
    """Calculates result of an expression."""
    try:
        result = expression_evaluator.evaluate(c_input.expression)
    except ValueError as e:
        logger.exception(f"Calculation error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

    return {"result": result}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
