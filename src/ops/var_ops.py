from src.utils import Error

variables = {}

local_scopes = []

def push_scope():
    """Create a new local scope (called when entering a function)"""
    local_scopes.append({})

def pop_scope():
    """Remove the current local scope (called when exiting a function)"""
    if local_scopes:
        local_scopes.pop()

def assign_local(stack):
    """Assign to local variable (only visible in current function)"""
    if len(stack) < 2:
        Error("StackUnderflow", "local requires a value and a name", "local")
        return
    name = stack.pop()
    val = stack.pop()
    
    if not isinstance(name, str):
        Error("TypeError", f"Variable name must be a string, got {type(name).__name__}", "local")
        stack.append(val)
        stack.append(name)
        return
    
    if local_scopes:
        local_scopes[-1][name] = val
    else:
        variables[name] = val

def assign_global(stack):
    """Assign to global variable (visible everywhere) - same as old ="""
    if len(stack) < 2:
        Error("StackUnderflow", "global requires a value and a name", "global")
        return
    name = stack.pop()
    val = stack.pop()
    
    if not isinstance(name, str):
        Error("TypeError", f"Variable name must be a string, got {type(name).__name__}", "global")
        stack.append(val)
        stack.append(name)
        return
    
    variables[name] = val

def assign(stack):
    """Old = command - defaults to global for backwards compatibility"""
    assign_global(stack)

def set_dynamic(stack):
    """
    Dynamic variable assignment - use string value as variable name.
    Stack effect: value name_string --
    Example: 42 "varname" set_dynamic  (sets variable named by string in varname)
    """
    if len(stack) < 2:
        Error("StackUnderflow", "set_dynamic requires a value and a name string", "set_dynamic")
        return
    
    name_var = stack.pop()  
    val = stack.pop()
    
    if not isinstance(name_var, str):
        Error("TypeError", f"set_dynamic expected string, got {type(name_var).__name__}", "set_dynamic")
        stack.append(val)
        stack.append(name_var)
        return
    
    variables[name_var] = val

def get_variable(name):
    """Get a variable, checking local scopes first, then global"""
    for scope in reversed(local_scopes):
        if name in scope:
            return scope[name], True
    
    if name in variables:
        return variables[name], True
    
    return None, False

def call(stack):
    """Get variable value (checks local then global)"""
    if not stack:
        Error("StackUnderflow", "call requires a variable name", "call")
        return
    
    name = stack.pop()
    
    if not isinstance(name, str):
        Error("TypeError", f"Variable name must be a string, got {type(name).__name__}", "call")
        stack.append(name)
        return
    
    value, found = get_variable(name)
    
    if found:
        stack.append(value)
    else:
        all_vars = set(variables.keys())
        for scope in local_scopes:
            all_vars.update(scope.keys())
        
        if all_vars:
            available = ", ".join(f"'{v}'" for v in list(all_vars)[:5])
            if len(all_vars) > 5:
                available += ", ..."
            Error("NameError", f"variable '{name}' is not defined. Available variables: {available}", "call")
        else:
            Error("NameError", f"variable '{name}' is not defined (no variables defined yet)", "call")

def get_dynamic(stack):
    if not stack:
        Error("StackUnderflow", "get_dynamic requires a name string", "get_dynamic")
        return
    
    name_var = stack.pop()  
    
    if not isinstance(name_var, str):
        Error("TypeError", f"get_dynamic expected string, got {type(name_var).__name__}", "get_dynamic")
        stack.append(name_var)
        return
    
    value, found = get_variable(name_var)
    
    if found:
        stack.append(value)
    else:
        Error("NameError", f"variable '{name_var}' is not defined", "get_dynamic")

def list_variables():
    """Helper function to list all defined variables (global and local)"""
    all_vars = set(variables.keys())
    for scope in local_scopes:
        all_vars.update(scope.keys())
    return list(all_vars)