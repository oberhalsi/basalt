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

def split_chars(stack):
    if not stack:
        Error("StackUnderflow", "split_chars requires a string", "split_chars")
        return
    
    s = stack.pop()
    
    if not isinstance(s, str):
        Error("TypeError", f"split_chars expected a string, got {type(s).__name__}", "split_chars")
        return
    

    for char in reversed(s):
        stack.append(char)
    
    stack.append(len(s))

def split_chars(stack):
    """
    Split a string into individual characters.
    Stack effect: str -- char1 char2 ... charN count
    
    To ensure 'h' is popped first, we push 'o' through 'h' in reverse.
    """
    if not stack:
        Error("StackUnderflow", "split_chars requires a string on the stack", "split_chars")
        return
    
    s = stack.pop()
    
    if not isinstance(s, str):
        Error("TypeError", f"split_chars expected a string, got {type(s).__name__}", "split_chars")
        return
    
    for char in reversed(s):
        stack.append(char)
    
    stack.append(len(s))