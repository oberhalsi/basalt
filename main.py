import sys
from src.lexer import tokenize
from src.parser import execute

def main():
    if len(sys.argv) < 2:
        return
    
    with open(sys.argv[1], 'r') as f:
        code = f.read()

    stack = []
    tokens = tokenize(code)
    execute(tokens, stack)

if __name__ == "__main__":
    main()