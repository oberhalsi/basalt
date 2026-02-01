from src.ops.math_ops import add, sub, mul, div, mod
from src.ops.io_ops import put, ask
from src.ops.stack_ops import dup, drop, swap, clear
from src.ops.logic_ops import eq, gt, lt
from src.ops.var_ops import assign, call
from src.utils import Error

CMDS = {
    # Math ops
    "+": lambda stack: add(stack),
    "-": lambda stack: sub(stack),
    "*": lambda stack: mul(stack),
    "/": lambda stack: div(stack),
    "%": lambda stack: mod(stack),
    # IO ops
    "print": lambda stack: put(stack),
    "in": lambda stack: ask(stack),
    # Stack ops
    "dup": lambda stack: dup(stack),
    "drop": lambda stack: drop(stack),
    "swap": lambda stack: swap(stack),
    "popall": lambda stack: clear(stack),
    # Boolean ops
    "==": lambda stack: eq(stack),
    ">": lambda stack: gt(stack),
    "<": lambda stack: lt(stack),
    # Variable ops
    "=": lambda stack: assign(stack),
    "call": lambda stack: call(stack),
}

def execute(tokens, stack, labels=None):
    if labels is None:
        labels = {t[:-1]: i for i, t in enumerate(tokens) if t.endswith(':')}
    
    pc = 0
    while pc < len(tokens):
        token = tokens[pc]

        if token == "{":
            block, depth = [], 1
            pc += 1
            while pc < len(tokens) and depth > 0:
                if tokens[pc] == "{": depth += 1
                elif tokens[pc] == "}": depth -= 1
                if depth > 0: block.append(tokens[pc])
                pc += 1
            stack.append(block)
            continue

        if token == "run":
            if not stack: Error("StackUnderflow", "nothing to run", "run")
            block = stack.pop()
            if isinstance(block, list):
                execute(block, stack, labels)
            pc += 1
            continue

        if token in CMDS:
            CMDS[token](stack)
        elif token == "jump":
            pc = labels[stack.pop()]
            continue 
        elif token == "if_jump":
            target, cond = stack.pop(), stack.pop()
            if cond:
                pc = labels[target]
                continue
        elif token.startswith('"') and token.endswith('"'):
            stack.append(token[1:-1])
        elif not token.endswith(':'):
            try: stack.append(int(token))
            except ValueError: pass
        pc += 1