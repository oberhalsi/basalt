from src.utils import Error

variables = {}

def assign(stack):
    if len(stack) < 2:
        Error("StackUnderflow", "= requires a value and a name", "=")
        return
    name = stack.pop()
    val = stack.pop()
    
    if not isinstance(name, str):
        Error("TypeError", f"Variable name must be a string, got {type(name).__name__}", "=")
        stack.append(val)  
        stack.append(name)  
        return
    
    variables[name] = val

def call(stack):
    if not stack:
        Error("StackUnderflow", "call requires a variable name", "call")
        return
    
    name = stack.pop()
    
    if not isinstance(name, str):
        Error("TypeError", f"Variable name must be a string, got {type(name).__name__}", "call")
        stack.append(name)  
        return
    
    if name in variables:
        stack.append(variables[name])
    else:
        # List available variables to help debugging
        if variables:
            available = ", ".join(f"'{v}'" for v in list(variables.keys())[:5])
            if len(variables) > 5:
                available += ", ..."
            Error("NameError", f"variable '{name}' is not defined. Available variables: {available}", "call")
        else:
            Error("NameError", f"variable '{name}' is not defined (no variables defined yet)", "call")

def list_variables():
    """Helper function to list all defined variables"""
    return list(variables.keys())