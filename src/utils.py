import re
import sys

def split_words(text):
    pattern = r'#.*|"(?:\\.|[^"\\])*"|\S+'
    tokens = []
    for match in re.finditer(pattern, text):
        token = match.group(0)
        if not token.startswith('#'):
            tokens.append(token)
    return tokens

def Error(errtype, message, cmd):
    print(f"Basalt Error: {errtype}")
    print(f"    '{cmd}'")
    print(f"{message}")
    sys.exit()