from src.utils import Error

def concat(stack):
    if len(stack) < 2:
        Error("StackUnderflowError", "CONCAT requires two elements on the stack.", "CONCAT")
    b = stack.pop()
    a = stack.pop()

    if not isinstance(a, str) or not isinstance(b, str):
        Error("TypeError", f"CONCAT expected two strings, but got {type(a).__name__} and {type(b).__name__}.", "CONCAT")

    result = a + b
    stack.append(result)