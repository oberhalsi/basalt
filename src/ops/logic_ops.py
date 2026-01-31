from src.utils import Error

def eq(stack):
    if len(stack) < 2:
        Error("StackUnderflow", "== requires two values to compare", "==")
        return
    b, a = stack.pop(), stack.pop()
    stack.append(1 if a == b else 0)

def gt(stack):
    if len(stack) < 2:
        Error("StackUnderflow", "> requires two values to compare", ">")
        return
    b, a = stack.pop(), stack.pop()
    # Note: Using try/except in the case that they try to compare a string and an int
    try:
        stack.append(1 if a > b else 0)
    except TypeError:
        Error("TypeError", f"Cannot compare {type(a).__name__} and {type(b).__name__}", ">")

def lt(stack):
    if len(stack) < 2:
        Error("StackUnderflow", "< requires two values to compare", "<")
        return
    b, a = stack.pop(), stack.pop()
    try:
        stack.append(1 if a < b else 0)
    except TypeError:
        Error("TypeError", f"Cannot compare {type(a).__name__} and {type(b).__name__}", "<")