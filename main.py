import sys
from src.lexer import tokenize
from src.parser import execute
from src.ops.include_ops import set_current_file_dir

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <file.b>")
        return
    
    filepath = sys.argv[1]
    
    set_current_file_dir(filepath)
    
    with open(filepath, 'r') as f:
        code = f.read()
    
    stack = []
    tokens = tokenize(code)
    execute(tokens, stack)

if __name__ == "__main__":
    main()