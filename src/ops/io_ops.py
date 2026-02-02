import sys
from src.utils import Error

did_print = False

def put(stack):
    if not stack:
        Error("StackUnderflow", "nothing to print (stack is empty)", "print")
        return
    print(stack.pop())

def dot(stack):
    if not stack:
        Error("StackUnderflow", "nothing to print (stack is empty)", ".")
        return
    sys.stdout.write(str(stack.pop()))

def ask(stack):
    try:
        user_input = input("> ") 
        
        # Try to treat it as a number if possible
        try:
            stack.append(int(user_input))
        except ValueError:
            stack.append(user_input)
            
    except EOFError:
        Error("IOError", "input stream closed", "in")
    except KeyboardInterrupt:
        print("\nInput cancelled.")