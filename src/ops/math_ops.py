from src.utils import Error

def add(stack):
    if len(stack) < 2:
        Error("StackUnderflow", "+ requires two values", "+")
        return
    b, a = stack.pop(), stack.pop()
    try:
        stack.append(a + b)
    except TypeError:
        Error("TypeError", f"Cannot add {type(a).__name__} and {type(b).__name__}", "+")

def sub(stack):
    if len(stack) < 2:
        Error("StackUnderflow", "- requires two values", "-")
        return
    b, a = stack.pop(), stack.pop()
    try:
        stack.append(a - b)
    except TypeError:
        Error("TypeError", f"Cannot subtract {type(b).__name__} from {type(a).__name__}", "-")

def mul(stack):
    if len(stack) < 2:
        Error("StackUnderflow", "* requires two values", "*")
        return
    b, a = stack.pop(), stack.pop()
    try:
        stack.append(a * b)
    except TypeError:
        Error("TypeError", f"Cannot multiply {type(a).__name__} by {type(b).__name__}", "*")

def div(stack):
    if len(stack) < 2:
        Error("StackUnderflow", "/ requires two values", "/")
        return
    b, a = stack.pop(), stack.pop()
    if b == 0:
        Error("MathError", "Division by zero", "/")
        # Push them back so the stack doesn't lose data on a failed op
        stack.append(a)
        stack.append(b)
        return
    try:
        stack.append(a // b)
    except TypeError:
        Error("TypeError", f"Cannot divide {type(a).__name__} by {type(b).__name__}", "/")

def mod(stack):
    if len(stack) < 2:
        Error("StackUnderflow", "% requires two values", "%")
        return
    b, a = stack.pop(), stack.pop()
    if b == 0:
        Error("MathError", "Modulo by zero", "%")
        return
    stack.append(a % b)