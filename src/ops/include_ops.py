import os
from src.utils import Error
from src.lexer import tokenize

# Track included files to prevent circular imports
_included_files = set()

# Track the directory of the currently executing file
_current_file_dir = None

def set_current_file_dir(filepath):
    """Set the directory of the file being executed"""
    global _current_file_dir
    if filepath:
        _current_file_dir = os.path.dirname(os.path.abspath(filepath))
    else:
        _current_file_dir = os.getcwd()

def include(stack, tokens, pc, labels):
    """
    Include a Basalt file and execute it in the current context.
    Syntax: "filename.b" include
    
    The file path is resolved in this order:
    1. Relative to the current file's directory
    2. Relative to the current working directory
    3. Absolute path if provided
    """
    global _current_file_dir
    
    if not stack:
        Error("StackUnderflow", "include requires a filename", "include")
        return pc + 1, tokens, labels
    
    filename = stack.pop()
    
    if not isinstance(filename, str):
        Error("TypeError", f"include expected a string filename, got {type(filename).__name__}", "include")
        return pc + 1, tokens, labels
    
    resolved_path = None
    
    if _current_file_dir:
        candidate = os.path.join(_current_file_dir, filename)
        if os.path.exists(candidate):
            resolved_path = candidate

    if not resolved_path and os.path.exists(filename):
        resolved_path = filename
    
    if not resolved_path:
        abs_filename = os.path.abspath(filename)
        if os.path.exists(abs_filename):
            resolved_path = abs_filename
    
    if not resolved_path:
        Error("FileNotFoundError", f"Could not find file '{filename}'", "include")
        return pc + 1, tokens, labels
    
    abs_path = os.path.abspath(resolved_path)
    
    if abs_path in _included_files:
        return pc + 1, tokens, labels
    
    try:
        with open(resolved_path, 'r') as f:
            code = f.read()
    except IOError as e:
        Error("IOError", f"Could not read file '{filename}': {e}", "include")
        return pc + 1, tokens, labels
    
    _included_files.add(abs_path)
    
    prev_dir = _current_file_dir
    set_current_file_dir(resolved_path)
    
    included_tokens = tokenize(code)
    
    new_labels = {}
    for i, t in enumerate(included_tokens):
        if t.endswith(':'):
            label_name = t[:-1]
            new_labels[label_name] = i + pc + 1
    
    labels.update(new_labels)
    
    tokens[pc+1:pc+1] = included_tokens
    
    _current_file_dir = prev_dir
    
    return pc + 1, tokens, labels


def reset_includes():
    """Reset the included files tracker (useful for REPL between executions)"""
    global _included_files
    _included_files.clear()