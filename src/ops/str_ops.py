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
    """
    Split a string into individual characters.
    Stack effect: str -- char1 char2 char3 ... count
    Example: "abc" split_chars → "c" "b" "a" 3
    
    Note: Characters are pushed in REVERSE order so that when popped,
    they come out in the correct order (a, b, c).
    """
    if not stack:
        Error("StackUnderflow", "split_chars requires a string", "split_chars")
        return
    
    s = stack.pop()
    
    if not isinstance(s, str):
        Error("TypeError", f"split_chars expected a string, got {type(s).__name__}", "split_chars")
        return
    
    # Push characters in REVERSE order so they pop in correct order
    for char in reversed(s):
        stack.append(char)
    
    # Push the count so the caller knows how many chars were pushed
    stack.append(len(s))

def int_to_str(stack):
    """
    Convert integer to string.
    Stack effect: int -- str
    Example: 42 int_to_str → "42"
    """
    if not stack:
        Error("StackUnderflow", "int_to_str requires an integer", "int_to_str")
        return
    
    n = stack.pop()
    
    if not isinstance(n, int):
        Error("TypeError", f"int_to_str expected an integer, got {type(n).__name__}", "int_to_str")
        return
    
    stack.append(str(n))

def str_to_int(stack):
    """
    Convert string to integer.
    Stack effect: str -- int
    Example: "42" str_to_int → 42
    """
    if not stack:
        Error("StackUnderflow", "str_to_int requires a string", "str_to_int")
        return
    
    s = stack.pop()
    
    if not isinstance(s, str):
        Error("TypeError", f"str_to_int expected a string, got {type(s).__name__}", "str_to_int")
        return
    
    try:
        n = int(s)
        stack.append(n)
    except ValueError:
        Error("ValueError", f"str_to_int cannot convert '{s}' to integer", "str_to_int")
        return