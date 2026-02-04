from src.utils import Error

def concat(stack):
    if len(stack) < 2:
        Error("StackUnderflow", "str+ requires two elements on the stack", "str+")
        return
    b = stack.pop()
    a = stack.pop()
    if not isinstance(a, str) or not isinstance(b, str):
        Error("TypeError", f"str+ expected two strings, but got {type(a).__name__} and {type(b).__name__}", "str+")
        return
    result = a + b
    stack.append(result)  
