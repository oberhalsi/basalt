from src.ops.math_ops import add, sub, mul, div, mod, power
from src.ops.io_ops import put, ask, dot, newline
from src.ops.stack_ops import dup, drop, swap, clear, pick, rot, over
from src.ops.logic_ops import eq, gt, lt, and_op, or_op, not_op, xor_op
from src.ops.var_ops import assign, call
import src.ops.var_ops as var_ops
from src.ops.str_ops import concat
from src.ops.include_ops import include
from src.utils import Error

CMDS = {
    # Math ops
    "+": lambda stack: add(stack),
    "-": lambda stack: sub(stack),
    "*": lambda stack: mul(stack),
    "/": lambda stack: div(stack),
    "%": lambda stack: mod(stack),
    "^": lambda stack: power(stack),
    
    # IO ops
    "print": lambda stack: put(stack),
    "in": lambda stack: ask(stack),
    ".": lambda stack: dot(stack),
    "newline": lambda stack: newline(stack),
    
    # Stack ops
    "dup": lambda stack: dup(stack),
    "drop": lambda stack: drop(stack),
    "swap": lambda stack: swap(stack),
    "pick": lambda stack: pick(stack),
    "rot": lambda stack: rot(stack),
    "over": lambda stack: over(stack),
    "popall": lambda stack: clear(stack),
    
    # Boolean ops
    "==": lambda stack: eq(stack),
    ">": lambda stack: gt(stack),
    "<": lambda stack: lt(stack),
    "and": lambda stack: and_op(stack),
    "or": lambda stack: or_op(stack),
    "not": lambda stack: not_op(stack),
    "xor": lambda stack: xor_op(stack),
    
    # Variable ops
    "=": lambda stack: assign(stack),
    "call": lambda stack: call(stack),
    
    # String ops
    "str+": lambda stack: concat(stack)
}

def validate_syntax(tokens):
    """
    Pre-validate tokens for common syntax errors before execution.
    Returns True if valid, False otherwise.
    """
    brace_depth = 0
    for i, token in enumerate(tokens):
        if token == "{":
            brace_depth += 1
        elif token == "}":
            brace_depth -= 1
            if brace_depth < 0:
                Error("SyntaxError", "Unexpected closing brace '}' without matching '{'", "}")
                return False
    
    if brace_depth > 0:
        Error("SyntaxError", f"Unclosed code block - missing {brace_depth} closing brace(s) '}}'", "{")
        return False
    
    for token in tokens:
        if token.startswith('"') and not token.endswith('"'):
            Error("SyntaxError", f"Unclosed string: {token}", token)
            return False
    
    return True

def execute(tokens, stack, labels=None):
    if not validate_syntax(tokens):
        return
    
    if labels is None:
        labels = {t[:-1]: i for i, t in enumerate(tokens) if t.endswith(':')}
    
    pc = 0
    while pc < len(tokens):
        token = tokens[pc]
        
        if token == "{":
            block, depth = [], 1
            pc += 1
            while pc < len(tokens) and depth > 0:
                if tokens[pc] == "{": 
                    depth += 1
                elif tokens[pc] == "}": 
                    depth -= 1
                if depth > 0: 
                    block.append(tokens[pc])
                pc += 1
            
            if depth > 0:
                Error("SyntaxError", "Unclosed code block (missing })", "{")
                return
            
            stack.append(block)
            continue
        
        if token == "}":
            Error("SyntaxError", "Unexpected '}' - not inside a code block", "}")
            return
        
        if token == "run":
            if not stack: 
                Error("StackUnderflow", "nothing to run", "run")
                pc += 1
                continue
            
            block = stack.pop()
            if not isinstance(block, list):
                Error("TypeError", f"'run' expected a code block, got {type(block).__name__}", "run")
                pc += 1
                continue
            
            block_labels = {t[:-1]: i for i, t in enumerate(block) if t.endswith(':')}
            
            combined_labels = labels.copy()
            combined_labels.update(block_labels)
            
            execute(block, stack, combined_labels)
            pc += 1
            continue
        

        if token == "include":
            pc, tokens, labels = include(stack, tokens, pc, labels)
            continue
        
        if token in CMDS:
            CMDS[token](stack)
        elif token == "jump":
            if not stack:
                Error("StackUnderflow", "jump requires a label", "jump")
            else:
                label = stack.pop()
                if not isinstance(label, str):
                    Error("TypeError", f"jump expected a string label, got {type(label).__name__}", "jump")
                elif label in labels:
                    pc = labels[label]
                    continue
                else:
                    Error("NameError", f"label '{label}' not found", "jump")
        elif token == "if_jump":
            if len(stack) < 2:
                Error("StackUnderflow", "if_jump requires a label and condition", "if_jump")
            else:
                target, cond = stack.pop(), stack.pop()
                if not isinstance(target, str):
                    Error("TypeError", f"if_jump expected a string label, got {type(target).__name__}", "if_jump")
                elif cond:
                    if target in labels:
                        pc = labels[target]
                        continue
                    else:
                        Error("NameError", f"label '{target}' not found", "if_jump")
        elif token.startswith('"') and token.endswith('"'):
            stack.append(token[1:-1])
        elif not token.endswith(':'):
            try: 
                stack.append(int(token))
            except ValueError:
                if token in var_ops.variables:
                    value = var_ops.variables[token]
                    if isinstance(value, list):
                        block_labels = {t[:-1]: i for i, t in enumerate(value) if t.endswith(':')}
                        combined_labels = labels.copy()
                        combined_labels.update(block_labels)
                        execute(value, stack, combined_labels)
                    else:
                        stack.append(value)
                else:
                    Error("NameError", f"Unknown identifier '{token}' - not a command or defined variable", token)
        
        pc += 1