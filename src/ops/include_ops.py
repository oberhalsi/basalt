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

def find_library(filename):
    """
    Find a library file.
    
    Search order:
    1. Check if it's in the libraries/ folder (standard library)
    2. Treat as a relative/absolute path
    3. Try adding .b extension if missing
    
    Returns: absolute path to file, or None if not found
    """
    # Determine the project root (where main.py is)
    # Assume current file dir or cwd contains the libraries folder
    if _current_file_dir:
        project_root = _current_file_dir
        # Walk up to find libraries folder
        temp = _current_file_dir
        while temp and temp != os.path.dirname(temp):
            if os.path.exists(os.path.join(temp, "libraries")):
                project_root = temp
                break
            temp = os.path.dirname(temp)
    else:
        project_root = os.getcwd()
    
    libraries_folder = os.path.join(project_root, "libraries")
    
    # 1. Check standard library folder first
    if os.path.exists(libraries_folder):
        # Try exact name
        lib_path = os.path.join(libraries_folder, filename)
        if os.path.exists(lib_path):
            return os.path.abspath(lib_path)
        
        # Try with .b extension
        if not filename.endswith('.b'):
            lib_path_with_ext = lib_path + '.b'
            if os.path.exists(lib_path_with_ext):
                return os.path.abspath(lib_path_with_ext)
    
    # 2. Try as relative/absolute path
    # If it's already an absolute path
    if os.path.isabs(filename):
        if os.path.exists(filename):
            return os.path.abspath(filename)
        if not filename.endswith('.b'):
            if os.path.exists(filename + '.b'):
                return os.path.abspath(filename + '.b')
    
    # Try relative to current file's directory
    if _current_file_dir:
        candidate = os.path.join(_current_file_dir, filename)
        if os.path.exists(candidate):
            return os.path.abspath(candidate)
        if not filename.endswith('.b'):
            if os.path.exists(candidate + '.b'):
                return os.path.abspath(candidate + '.b')
    
    # Try relative to current working directory
    if os.path.exists(filename):
        return os.path.abspath(filename)
    if not filename.endswith('.b'):
        if os.path.exists(filename + '.b'):
            return os.path.abspath(filename + '.b')
    
    return None

def include(stack, tokens, pc, labels):
    """
    Include a Basalt file and execute it in the current context.
    Syntax: "filename" include
    """
    global _current_file_dir
    
    if not stack:
        Error("StackUnderflow", "include requires a filename", "include")
        return pc + 1, tokens, labels
    
    filename = stack.pop()
    
    if not isinstance(filename, str):
        Error("TypeError", f"include expected a string filename, got {type(filename).__name__}", "include")
        return pc + 1, tokens, labels
    
    # Find the library
    resolved_path = find_library(filename)
    
    if not resolved_path:
        Error("FileNotFoundError", f"Could not find file '{filename}' in libraries/ or as a path", "include")
        return pc + 1, tokens, labels
    
    # Check for circular imports
    abs_path = os.path.abspath(resolved_path)
    if abs_path in _included_files:
        # Silently skip already included files
        return pc + 1, tokens, labels
    
    # Try to open and read the file
    try:
        with open(resolved_path, 'r') as f:
            code = f.read()
    except IOError as e:
        Error("IOError", f"Could not read file '{filename}': {e}", "include")
        return pc + 1, tokens, labels
    
    # Mark this file as included
    _included_files.add(abs_path)
    
    # Save the previous directory and set new one
    prev_dir = _current_file_dir
    set_current_file_dir(resolved_path)
    
    # Tokenize the included file
    included_tokens = tokenize(code)
    
    # Extract any labels from the included file and merge them
    new_labels = {}
    for i, t in enumerate(included_tokens):
        if t.endswith(':'):
            label_name = t[:-1]
            new_labels[label_name] = i + pc + 1
    
    labels.update(new_labels)
    
    # Insert the included tokens right after the current position
    tokens[pc+1:pc+1] = included_tokens
    
    # Restore the previous directory
    _current_file_dir = prev_dir
    
    # Return updated pc
    return pc + 1, tokens, labels


def reset_includes():
    """Reset the included files tracker (useful for REPL between executions)"""
    global _included_files
    _included_files.clear()