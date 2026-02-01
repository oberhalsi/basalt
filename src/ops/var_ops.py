from src.utils import Error

variables = {}

def assign(stack):
    if len(stack) < 2:
        Error("StackUnderflow", "= requires a value and a name", "=")
    name = stack.pop()
    val = stack.pop()
    variables[name] = val

def call(stack):
    if not stack:
        Error("StackUnderflow", "call requires a variable name", "call")
    name = stack.pop()
    if name in variables:
        stack.append(variables[name])
    else:
        Error("NameError", f"variable '{name}' is not defined", "call")