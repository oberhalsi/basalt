# Error Types

Basalt provides comprehensive error checking with clear, helpful error messages.

---

## Syntax Errors

### Unclosed Code Block
**Error:** Missing closing brace `}`

**Example:**
```basalt
{ "Hello" print
```

**Error Message:**
```
==================================================
Basalt Error: SyntaxError
==================================================
Command: '{'
Message: Unclosed code block - missing 1 closing brace(s) '}'
==================================================
```

**Fix:**
```basalt
{ "Hello" print }
```

---

### Unexpected Closing Brace
**Error:** Closing brace `}` without matching opening `{`

**Example:**
```basalt
"Hello" print }
```

**Error Message:**
```
==================================================
Basalt Error: SyntaxError
==================================================
Command: '}'
Message: Unexpected closing brace '}' without matching '{'
==================================================
```

**Fix:**
```basalt
{ "Hello" print }
# or just:
"Hello" print
```

---

### Unknown Token
**Error:** Token that isn't a command, number, or string

**Example:**
```basalt
thisIsNotACommand
```

**Error Message:**
```
==================================================
Basalt Error: SyntaxError
==================================================
Command: 'thisIsNotACommand'
Message: Unknown token 'thisIsNotACommand' - not a command, number, or string
==================================================
```

**Fix:**
```basalt
"thisIsAString" print
# or define it first:
{ "Hello" print } "thisIsAFunction" =
```

---

## Stack Underflow Errors

### Not Enough Values for Operation
**Error:** Operation needs more values than are on the stack

**Example:**
```basalt
5 + +    # Only one value, but + needs two
```

**Error Message:**
```
==================================================
Basalt Error: StackUnderflow
==================================================
Command: '+'
Message: + requires two values
==================================================
```

**Fix:**
```basalt
5 10 + +    # Now there are enough values
# or:
5 10 +      # Just one addition
```

---

### Empty Stack Operations
**Error:** Trying to operate on empty stack

**Example:**
```basalt
dup    # Nothing to duplicate
```

**Error Message:**
```
==================================================
Basalt Error: StackUnderflow
==================================================
Command: 'dup'
Message: nothing to duplicate
==================================================
```

**Fix:**
```basalt
5 dup    # Now there's something to duplicate
```

---

## Type Errors

### Wrong Type for Run
**Error:** Trying to run something that isn't a code block

**Example:**
```basalt
5 run
```

**Error Message:**
```
==================================================
Basalt Error: TypeError
==================================================
Command: 'run'
Message: 'run' expected a code block, got int
==================================================
```

**Fix:**
```basalt
{ 5 print } run
```

---

### String + Number
**Error:** Cannot add string and number

**Example:**
```basalt
"hello" 5 +
```

**Error Message:**
```
==================================================
Basalt Error: TypeError
==================================================
Command: '+'
Message: Cannot add str and int
==================================================
```

**Fix:**
```basalt
# Either both strings:
"hello" "5" str+

# Or both numbers:
5 10 +
```

---

### Wrong Variable Name Type
**Error:** Variable name must be a string

**Example:**
```basalt
5 10 =    # Trying to use 5 as variable name
```

**Error Message:**
```
==================================================
Basalt Error: TypeError
==================================================
Command: '='
Message: Variable name must be a string, got int
==================================================
```

**Fix:**
```basalt
5 "ten" =
```

---

### Wrong Label Type
**Error:** Label must be a string

**Example:**
```basalt
123 jump
```

**Error Message:**
```
==================================================
Basalt Error: TypeError
==================================================
Command: 'jump'
Message: jump expected a string label, got int
==================================================
```

**Fix:**
```basalt
"my_label" jump
```

---

### Incompatible Type Comparison
**Error:** Cannot compare string and number

**Example:**
```basalt
"hello" 5 >
```

**Error Message:**
```
==================================================
Basalt Error: TypeError
==================================================
Command: '>'
Message: Cannot compare str and int
==================================================
```

**Fix:**
```basalt
# Compare same types:
5 10 >
"hello" "world" >
```

---

## Name Errors

### Undefined Variable
**Error:** Variable hasn't been defined

**Example:**
```basalt
"undefined_var" call
```

**Error Message (no variables defined):**
```
==================================================
Basalt Error: NameError
==================================================
Command: 'call'
Message: variable 'undefined_var' is not defined (no variables defined yet)
==================================================
```

**Error Message (with existing variables):**
```
==================================================
Basalt Error: NameError
==================================================
Command: 'call'
Message: variable 'undefined_var' is not defined. Available variables: 'square', 'cube', 'double'
==================================================
```

**Fix:**
```basalt
# Define it first
10 "my_var" =
"my_var" call
```

---

### Label Not Found
**Error:** Jump target doesn't exist

**Example:**
```basalt
"nonexistent_label" jump
```

**Error Message:**
```
==================================================
Basalt Error: NameError
==================================================
Command: 'jump'
Message: label 'nonexistent_label' not found
==================================================
```

**Fix:**
```basalt
"my_label" jump
my_label:
    "Here!" print
```

---

## Math Errors

### Division by Zero
**Error:** Attempting to divide by zero

**Example:**
```basalt
10 0 /
```

**Error Message:**
```
==================================================
Basalt Error: MathError
==================================================
Command: '/'
Message: Division by zero
==================================================
```

**Fix:**
```basalt
# Check before dividing
denominator 0 == { "Cannot divide by zero" print } { 10 denominator / print } if_jump
```

**Note:** On division by zero, values are pushed back to preserve stack state.

---

### Modulo by Zero
**Error:** Attempting modulo by zero

**Example:**
```basalt
10 0 %
```

**Error Message:**
```
==================================================
Basalt Error: MathError
==================================================
Command: '%'
Message: Modulo by zero
==================================================
```

**Fix:**
```basalt
10 3 %    # Use non-zero divisor
```

---

### Zero to Negative Power
**Error:** 0 raised to a negative power

**Example:**
```basalt
0 -1 ^
```

**Error Message:**
```
==================================================
Basalt Error: MathError
==================================================
Command: '**'
Message: Zero cannot be raised to a negative power
==================================================
```

**Fix:**
```basalt
2 -1 ^    # Use non-zero base
```

---

### Overflow
**Error:** Result too large to represent

**Example:**
```basalt
999999999999 999999999999 ^
```

**Error Message:**
```
==================================================
Basalt Error: MathError
==================================================
Command: '**'
Message: Result too large
==================================================
```

**Fix:**
Use smaller numbers or implement arbitrary precision arithmetic.

---

## File Errors

### File Not Found
**Error:** Include file doesn't exist

**Example:**
```basalt
"nonexistent.b" include
```

**Error Message:**
```
==================================================
Basalt Error: FileNotFoundError
==================================================
Command: 'include'
Message: Could not find file 'nonexistent.b'
==================================================
```

**Fix:**
```basalt
# Check file path and name
"existing_file.b" include
```

---

### IO Error
**Error:** Cannot read file

**Example:**
```basalt
"protected_file.b" include
```

**Error Message:**
```
==================================================
Basalt Error: IOError
==================================================
Command: 'include'
Message: Could not read file 'protected_file.b': Permission denied
==================================================
```

**Fix:**
Check file permissions and accessibility.

---

### Input Error
**Error:** Input stream closed or interrupted

**Example:**
```basalt
in    # But input is closed (EOF)
```

**Error Message:**
```
==================================================
Basalt Error: IOError
==================================================
Command: 'in'
Message: input stream closed
==================================================
```

---

## Common Error Patterns and Solutions

### Pattern 1: Forgetting to Define
**Problem:**
```basalt
"func" call run    # ERROR: not defined
```

**Solution:**
```basalt
{ "Hello" print } "func" =
"func" call run    # ✓ Works
```

---

### Pattern 2: Wrong Stack Order
**Problem:**
```basalt
10 "value" =    # ERROR: name should be on top
```

**Solution:**
```basalt
10 "value" =    # ✓ Value first, then name
```

---

### Pattern 3: Mixing Types
**Problem:**
```basalt
"10" 5 +    # ERROR: string + number
```

**Solution:**
```basalt
10 5 +      # ✓ Both numbers
# or:
"10" "5" str+    # ✓ Both strings
```

---

### Pattern 4: Not Enough Values
**Problem:**
```basalt
5 + + +    # ERROR: not enough values
```

**Solution:**
```basalt
5 10 + 15 + 20 +    # ✓ Enough values for all operations
```

---

### Pattern 5: Unclosed Blocks
**Problem:**
```basalt
{ "Hello" print
"World" print
```

**Solution:**
```basalt
{ "Hello" print
  "World" print
}    # ✓ Closed properly
```

---

## Error Prevention Tips

### 1. Check Stack Depth
Before operations that need multiple values:
```basalt
# Good practice
a b +    # Make sure a and b exist

# Better with check (if you implement stack depth checking)
stack_size 2 >= { a b + } { "Not enough values!" print } if_jump
```

---

### 2. Validate Input Types
```basalt
# Check before operations
value 0 == { "Cannot use zero!" print } { 100 value / print } if_jump
```

---

### 3. Define Before Use
```basalt
# Always define first
{ dup * } "square" =

# Then use
5 "square" call run
```

---

### 4. Match Braces
```basalt
# Use proper formatting
{
    code here
}

# Not:
{ code here
```

---

### 5. Use Descriptive Names
```basalt
# Good - clear what went wrong
"calculate_average" call

# Bad - unclear
"calc" call
```

---

## Debugging Checklist

When you get an error:

1. **Read the error message** - It tells you what went wrong
2. **Check the command** - Which operation failed?
3. **Verify stack state** - Do you have enough values?
4. **Check types** - Are types compatible?
5. **Look for typos** - Variable names, label names, file names
6. **Check definitions** - Is it defined before use?
7. **Match braces** - All `{` have matching `}`?
8. **Test incrementally** - Add code piece by piece

---

## Verbose Error Mode

For detailed debugging, enable verbose errors in main.py:

```python
from src.utils import set_verbose_errors
set_verbose_errors(True)
```

This shows stack state in error messages.

---

## Getting Help

If you're stuck:

1. Read the error message carefully
2. Check the documentation for that command
3. Try a minimal example
4. Break down complex code into smaller pieces
5. Print intermediate values to debug