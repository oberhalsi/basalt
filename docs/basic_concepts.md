# Basic Concepts

## What is Basalt?

Basalt is a **stack-based programming language**. Instead of variables holding values, values are stored on a stack, and operations work on the stack.

---

## The Stack

### What is a Stack?

A stack is like a stack of plates - you can only add (push) or remove (pop) from the top.

**Example:**
```basalt
5          # Stack: [5]
10         # Stack: [5, 10]
+          # Stack: [15]
```

### Stack Visualization

```
Start:        []
5       →     [5]
10      →     [5, 10]
+       →     [15]
print   →     []
Output: 15
```

---

## Data Types

### Numbers
Integers only (for now):
```basalt
42
-10
0
999
```

### Strings
Text in double quotes:
```basalt
"Hello"
"Hello, World!"
"123"
""
```

### Code Blocks
Executable code in braces:
```basalt
{ 5 10 + }
{ "Hello" print }
```

---

## Comments

Comments start with `#` and go to end of line:
```basalt
# This is a comment
5 10 +  # This adds 5 and 10
```

---

## Basic Program Structure

### Simple Program
```basalt
# Print a message
"Hello, World!" print
```

### Program with Variables
```basalt
# Store a value
42 "answer" =

# Use it
"The answer is: " . "answer" call print
```

### Program with Functions
```basalt
# Define function
{ dup * } "square" =

# Use function
5 "square" call run print
```

---

## How Basalt Executes

### Step by Step

**Program:**
```basalt
5 10 + print
```

**Execution:**
1. Push 5 → Stack: `[5]`
2. Push 10 → Stack: `[5, 10]`
3. Add → Stack: `[15]`
4. Print → Stack: `[]`, Output: `15`

---

## Writing Your First Program

### Hello World
```basalt
"Hello, World!" print
```

### Calculator
```basalt
5 10 + print    # 15
10 3 - print    # 7
4 5 * print     # 20
10 2 / print    # 5
```

### With Variables
```basalt
100 "score" =
"Your score: " . "score" call print
```

---

## Common Patterns

### Print Multiple Things
```basalt
"Name: " . "Alice" print
"Age: " . 25 print
```

### Do Math
```basalt
# Square a number
5 dup *  # 25

# Average of two numbers
10 20 + 2 /  # 15
```

### Store and Reuse
```basalt
{ dup * } "square" =
5 "square" call run  # 25
```

---

## Understanding Stack Order

### Order Matters!
```basalt
10 3 -     # 10 - 3 = 7
3 10 -     # 3 - 10 = -7

10 2 /     # 10 / 2 = 5
2 10 /     # 2 / 10 = 0
```

### Fixing Order with `swap`
```basalt
3 10 swap -    # 10 - 3 = 7
2 10 swap /    # 10 / 2 = 5
```

---

## Reading Stack Notation

Documentation uses this format:

**`a b -- c`**
- Left of `--` = what goes in (bottom to top)
- Right of `--` = what comes out

**Examples:**
- `a b -- (a+b)` = takes 2 values, returns sum
- `a -- a a` = takes 1 value, returns 2 copies
- `a --` = takes 1 value, returns nothing

---

## Program Flow

### Sequential
Code runs top to bottom:
```basalt
"First" print
"Second" print
"Third" print
```

### Conditional
Use `if_jump` for conditions:
```basalt
x 0 > "positive" if_jump
"Not positive" print
"done" jump

positive:
    "Positive" print

done:
```

### Loops
Use labels and jumps:
```basalt
0 "i" =

loop:
    "i" call 5 < "continue" if_jump
    "done" jump

continue:
    "i" call print
    "i" call 1 + "i" =
    "loop" jump

done:
```

---

## Best Practices

### 1. Use Descriptive Names
```basalt
# Good
100 "max_score" =

# Bad
100 "x" =
```

### 2. Comment Your Code
```basalt
# Calculate area of circle
# Formula: π * r²
radius 314 * 100 /
```

### 3. Test Small Pieces
```basalt
# Test calculation first
5 5 * print    # Should be 25

# Then store as function
{ dup * } "square" =
```

### 4. Keep Stack Clean
```basalt
# Good - clean stack at end
5 10 + print

# Bad - leaves value on stack
5 10 +
```

---

## Common Mistakes

### 1. Forgetting Stack Order
```basalt
# Wrong
value 100 =    # Tries to use 100 as name

# Right
100 "value" =
```

### 2. Not Closing Braces
```basalt
# Wrong
{ "Hello" print

# Right
{ "Hello" print }
```

### 3. Using Numbers as Names
```basalt
# Wrong
10 5 =

# Right
10 "five" =
```

### 4. Forgetting to Run Blocks
```basalt
# Wrong - just puts block on stack
{ "Hello" print }

# Right - executes the block
{ "Hello" print } run
```

---

## Next Steps

1. **Try examples** - Type them and run them
2. **Read operation docs** - Learn each command
3. **Write small programs** - Practice makes perfect
4. **Build projects** - Make something useful!

---

## Quick Reference

### Print
```basalt
"Hello" print
```

### Variables
```basalt
42 "x" =
"x" call
```

### Functions
```basalt
{ dup * } "square" =
5 "square" call run
```

### Conditions
```basalt
condition "label" if_jump
```

### Loops
```basalt
loop:
    condition "done" if_jump
    # code
    "loop" jump
done:
```

---

## Getting Help

- Read the [INDEX.md](INDEX.md) to find specific topics
- Check [EXAMPLES.md](EXAMPLES.md) for working code
- Look at [ERROR_TYPES.md](ERROR_TYPES.md) when stuck

Happy coding! 🪨