# Code Blocks

## { } (Code Block)
**Stack Effect:** `-- block`

Creates a code block (list of tokens) and pushes it to the stack.

**Syntax:**
```basalt
{ code here }
```

**Examples:**
```basalt
{ 5 10 + }              # Block that adds 5 and 10
{ "Hello" print }       # Block that prints "Hello"
{ dup * }               # Block that squares a number
```

**Important Notes:**
- Code blocks are NOT executed when created
- They are data on the stack
- Must use `run` to execute them
- Can be stored in variables
- Can contain any valid Basalt code

---

## run (Execute Code Block)
**Stack Effect:** `block --`

Executes the code block on top of the stack.

**Examples:**
```basalt
{ 5 10 + print } run        # → 15

{ "Hello" print } run       # → Hello

5 { dup * } run print       # → 25
```

**Errors:**
- StackUnderflow: If stack is empty
- TypeError: If top of stack is not a code block

**Common Uses:**
```basalt
# Execute immediately
{ code } run

# Store and execute later
{ code } "function" =
"function" call run

# Conditional execution
condition { code } run
```

---

## Basic Code Block Usage

### 1. Simple Execution
```basalt
{ "Hello, World!" print } run
```

---

### 2. Store as Variable (Function)
```basalt
{ dup * } "square" =
5 "square" call run print    # → 25
```

---

### 3. Conditional Execution
```basalt
x 0 > 
{ "Positive" print }
{ "Not positive" print }
if_jump
```

---

## Code Blocks as Functions

### Defining Functions
```basalt
# Square function
{ dup * } "square" =

# Double function
{ 2 * } "double" =

# Print with newline
{ print newline } "println" =
```

### Using Functions
```basalt
5 "square" call run print       # → 25
10 "double" call run print      # → 20
"Hello" "println" call run      # → Hello\n
```

---

## Advanced Patterns

### 1. Function Composition
```basalt
{ 2 * } "double" =
{ 1 + } "inc" =

# Square, then double, then increment
{ "square" call run "double" call run "inc" call run } "f" =

5 "f" call run print    # → 51 (5² = 25, 25*2 = 50, 50+1 = 51)
```

---

### 2. Parameterized Code Blocks
```basalt
# Takes one parameter from stack
{ dup * } "square" =

# Takes two parameters from stack
{ + } "add" =
{ * } "multiply" =

5 10 "add" call run print       # → 15
5 10 "multiply" call run print  # → 50
```

---

### 3. Nested Code Blocks
```basalt
{
    5 10 +
    { dup * } run
    print
} run
# Calculates (5+10)² = 225
```

---

### 4. Closures (Sort of)
```basalt
# Store a value
10 "x" =

# Create function that uses x
{ "x" call * } "multiply_by_x" =

5 "multiply_by_x" call run print    # → 50
```

---

### 5. Higher-Order Patterns
```basalt
# Apply function twice
{ "f" call run "f" call run } "apply_twice" =

{ 2 * } "f" =
5 "apply_twice" call run print    # 5 * 2 * 2 = 20
```

---

## Conditional Execution with Code Blocks

### If-Then Pattern
```basalt
condition
{ "True branch" print }
run
```

### If-Else Pattern (Manual)
```basalt
condition
{ "True branch" print }
{ "False branch" print }
if_jump
```

### Better If-Else with Code Blocks
```basalt
# Store both branches
{ "True" print } "true_branch" =
{ "False" print } "false_branch" =

condition
"true_branch" call
"false_branch" call
if_jump
```

---

## Code Blocks vs Labels/Jumps

### Using Labels (Traditional)
```basalt
x 0 > "positive" if_jump
"Negative or zero" print
"done" jump

positive:
    "Positive" print

done:
```

### Using Code Blocks (Functional)
```basalt
x 0 >
{ "Positive" print }
{ "Negative or zero" print }
if_jump
```

**Comparison:**
- **Labels:** More explicit, traditional control flow
- **Code Blocks:** More functional, composable

---

## Common Code Block Patterns

### 1. Reusable Operations
```basalt
# Define once
{ dup * } "square" =
{ dup dup * * } "cube" =

# Use many times
3 "square" call run print
3 "cube" call run print
4 "square" call run print
4 "cube" call run print
```

---

### 2. Conditional Logic
```basalt
{ "Admin access granted" print } "admin_action" =
{ "User access granted" print } "user_action" =

is_admin
"admin_action" call
"user_action" call
if_jump
```

---

### 3. Callback-Style Programming
```basalt
# Define callbacks
{ "Processing started" print } "on_start" =
{ "Processing complete" print } "on_complete" =

# Use them
"on_start" call run
# ... do work ...
"on_complete" call run
```

---

### 4. Building Libraries
```basalt
# Math library
{ dup * } "square" =
{ dup dup * * } "cube" =
{ 2 * } "double" =
{ 2 / } "half" =

# String library
{ print newline } "println" =
{ ">> " swap str+ print } "bullet" =
```

---

### 5. Loop Bodies
```basalt
{ 
    "i" call print
    "i" call 1 + "i" =
} "loop_body" =

0 "i" =

loop:
    "i" call 10 < "continue" if_jump
    "done" jump

continue:
    "loop_body" call run
    "loop" jump

done:
```

---

## Nested Code Blocks

### Example 1: Block within Block
```basalt
{
    5 10 +
    { dup * } run
    print
} run
# Output: 225
```

### Example 2: Conditional in Block
```basalt
{
    "i" call 2 % 0 ==
    { "Even" print }
    { "Odd" print }
    if_jump
} "check_even_odd" =

5 "i" =
"check_even_odd" call run    # → Odd

6 "i" =
"check_even_odd" call run    # → Even
```

---

## Code Block Errors

### 1. Unclosed Block
```basalt
{ "Hello" print    # ERROR: Unclosed code block
```

### 2. Extra Closing Brace
```basalt
"Hello" print }    # ERROR: Unexpected '}'
```

### 3. Running Non-Block
```basalt
5 run    # ERROR: 'run' expected a code block, got int
```

### 4. Empty Stack
```basalt
run      # ERROR: nothing to run
```

---

## Best Practices

### 1. Use Descriptive Variable Names
```basalt
# Good
{ dup * } "square" =

# Bad
{ dup * } "s" =
```

---

### 2. Keep Blocks Simple
```basalt
# Good - simple, clear
{ 2 * } "double" =

# Bad - too complex in one block
{ dup 2 * swap 1 + swap / } "complex_calc" =
```

---

### 3. Comment Complex Blocks
```basalt
# Calculate distance: sqrt((x2-x1)² + (y2-y1)²)
{
    # Get differences
    "x2" call "x1" call -
    "y2" call "y1" call -
    
    # Square them
    swap dup * swap dup *
    
    # Sum and print
    + print
} "distance" =
```

---

### 4. Use Blocks for Readability
```basalt
# Instead of inline code
x 0 > "pos" if_jump
"Negative" print
"done" jump
pos: "Positive" print
done:

# Use blocks for clarity
x 0 >
{ "Positive" print }
{ "Negative" print }
if_jump
```

---

## Comparison with Other Languages

### Python Functions
**Python:**
```python
def square(x):
    return x * x

result = square(5)
```

**Basalt:**
```basalt
{ dup * } "square" =
5 "square" call run
```

---

### JavaScript Functions
**JavaScript:**
```javascript
const double = (x) => x * 2;
console.log(double(10));
```

**Basalt:**
```basalt
{ 2 * } "double" =
10 "double" call run print
```

---

### Lambda Functions
**Python:**
```python
apply_twice = lambda f, x: f(f(x))
double = lambda x: x * 2
print(apply_twice(double, 5))
```

**Basalt:**
```basalt
{ "f" call run "f" call run } "apply_twice" =
{ 2 * } "f" =
5 "apply_twice" call run print
```

---

## Tips and Tricks

1. **Test blocks independently** - Run them directly before storing
2. **Use blocks for conditional code** - Cleaner than labels sometimes
3. **Build libraries with blocks** - Reusable, composable code
4. **Stack hygiene** - Make sure blocks leave stack in expected state
5. **Document complex blocks** - Future you will thank you

---

## Limitations

**Code blocks cannot:**
- Modify their own code (no self-modifying code)
- Access local scope (all variables are global)
- Return values directly (must leave on stack)
- Be inspected/printed (will show as object representation)

**Future enhancements could add:**
- Block inspection
- Partial application
- Better closure support
- Named parameters