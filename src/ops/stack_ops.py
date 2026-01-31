from src.utils import Error

def dup(stack):
    if not stack:
        Error("StackUnderflow", "nothing to duplicate", "dup")
        return
    stack.append(stack[-1])

def drop(stack):
    if not stack:
        Error("StackUnderflow", "nothing to drop", "drop")
        return
    stack.pop()

def swap(stack):
    if len(stack) < 2:
        Error("StackUnderflow", "swap requires at least two items", "swap")
        return
    stack[-1], stack[-2] = stack[-2], stack[-1]

def clear(stack):
    stack.clear()