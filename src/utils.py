import re
import sys

# Track if we're in verbose error mode
VERBOSE_ERRORS = False

def set_verbose_errors(verbose):
    """Enable or disable verbose error messages"""
    global VERBOSE_ERRORS
    VERBOSE_ERRORS = verbose

def split_words(text):
    pattern = r'#.*|"(?:\\.|[^"\\])*"|\S+'
    tokens = []
    for match in re.finditer(pattern, text):
        token = match.group(0)
        if not token.startswith('#'):
            tokens.append(token)
    return tokens

def Error(errtype, message, cmd, stack=None):
    """
    Print a formatted error message.
    
    Args:
        errtype: Type of error (e.g., "SyntaxError", "StackUnderflow")
        message: Detailed error message
        cmd: The command/token that caused the error
        stack: Optional stack state for debugging
    """
    print(f"\n{'='*50}")
    print(f"Basalt Error: {errtype}")
    print(f"{'='*50}")
    print(f"Command: '{cmd}'")
    print(f"Message: {message}")
    
    if VERBOSE_ERRORS and stack is not None:
        print(f"\nStack state (top to bottom):")
        if stack:
            for i, item in enumerate(reversed(stack[-5:])):  
                item_str = str(item)
                if len(item_str) > 50:
                    item_str = item_str[:47] + "..."
                print(f"  [{len(stack) - i - 1}] {item_str}")
        else:
            print(f"  (empty)")
    
    print(f"{'='*50}\n")
    sys.exit()

def Warning(message):
    """Print a warning message"""
    print(f"⚠️  Warning: {message}")