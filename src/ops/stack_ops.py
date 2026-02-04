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

def pick(stack):
    try:
        n = stack.pop() 
    except IndexError:  
        Error("StackUnderflow", "pick requires at least one item", "pick")
        return
    if len(stack) >= n:
        stack.append(stack[-n])
    else:
        Error("StackUnderflow", f"stack too shallow for {n} pick", "pick")

def rot(stack):
    try:
        item = stack.pop(-3)
        stack.append(item)
    except IndexError:
        Error("StackUnderflow", "stack too shallow for rot", "rot")

def over(stack):
    try:
        stack.append(stack[-2])
    except IndexError:
        Error("StackUnderflow", "stack too shallow for over", "over")

def clear(stack):
    stack.clear()  
