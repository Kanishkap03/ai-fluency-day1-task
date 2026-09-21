import ast
import operator
from config import EXPENSES

def get_expense(category: str) -> str:
    """Look up this month's expense for one category."""
    for name, amount in EXPENSES.items():
        if name.lower() == category.strip().lower():
            return str(amount)
    return f"Unknown category: {category}"

# A safe calculator: only numbers and + - * / ( ) are allowed. Never use eval().
_OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
        ast.Div: operator.truediv, ast.USub: operator.neg}

def _evaluate(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_evaluate(node.left), _evaluate(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_evaluate(node.operand))
    raise ValueError("Unsupported expression")

def calculator(expression: str) -> str:
    """Evaluate a basic arithmetic expression such as (3500 + 1200) * 0.9."""
    try:
        return str(_evaluate(ast.parse(expression, mode="eval").body))
    except Exception as error:
        return f"Calculator error: {error}"

TOOL_FUNCTIONS = {"get_expense": get_expense, "calculator": calculator}

# These descriptions are what the LLM reads when deciding which tool to call
TOOLS = [
    {"type": "function", "function": {
        "name": "get_expense",
        "description": "Get this month's expense in rupees for one category, for example Food.",
        "parameters": {"type": "object",
                       "properties": {"category": {"type": "string"}},
                       "required": ["category"]}}},
    {"type": "function", "function": {
        "name": "calculator",
        "description": "Evaluate an arithmetic expression using + - * / and brackets.",
        "parameters": {"type": "object",
                       "properties": {"expression": {"type": "string"}},
                       "required": ["expression"]}}},
]

if __name__ == "__main__":
    print("get_expense('food') ->", get_expense("food"))
    print("calculator('(3500 + 1200) * 0.9') ->", calculator("(3500 + 1200) * 0.9"))
    print("calculator('6000 - 3500') ->", calculator("6000 - 3500"))
