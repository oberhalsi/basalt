# I/O Operations

## print (Print with Newline)
**Stack Effect:** `a --`

Prints the top value and removes it from the stack, adds a newline.

**Examples:**
```basalt
"Hello" print           # Output: Hello\n
42 print                # Output: 42\n
5 10 + print            # Output: 15\n
```

**Errors:**
- StackUnderflow: If stack is empty

**Common Uses:**
```basalt
"Result: " . 5 10 + print
"Hello, World!" print
```

---

## . (Dot - Print without Newline)
**Stack Effect:** `a --`

Prints the top value without a newline (useful for inline output).

**Examples:**
```basalt
"Hello" . " " . "World" print    # Output: Hello World\n
5 . " + " . 10 . " = " . 15 print # Output: 5 + 10 = 15\n
```

**Errors:**
- StackUnderflow: If stack is empty

**Common Uses:**
```basalt
# Build a line of output
"Name: " . "Alice" print

# Math expression
5 . " squared is " . 5 5 * print
```

---

## newline (Print Blank Line)
**Stack Effect:** `--`

Prints a blank line (just a newline character).

**Examples:**
```basalt
"Line 1" print
newline
"Line 3" print
```

**Output:**
```
Line 1

Line 3
```

**Common Uses:**
```basalt
# Separate sections
"Section 1" print
newline
"Section 2" print
```

---

## in (Input)
**Stack Effect:** `-- value`

Reads a line from standard input. Tries to parse as integer; if that fails, stores as string.

**Examples:**
```basalt
"Enter a number: " .
in                      # User types: 42
5 + print               # Output: 47

"What's your name? " .
in                      # User types: Alice
"Hello, " swap str+ print  # Output: Hello, Alice
```

**Behavior:**
- If input is a valid integer: pushes integer
- If input is not a valid integer: pushes string
- On EOF: raises IOError
- On Ctrl+C: prints "Input cancelled"

**Errors:**
- IOError: If input stream is closed
- KeyboardInterrupt: If user cancels (Ctrl+C)

**Common Uses:**
```basalt
# Get number input
"Enter age: " . in

# Get string input
"Enter name: " . in

# Input loop
loop:
    "Enter value (0 to quit): " . in
    dup 0 == { drop } { print "loop" jump } if_jump
```

---

## Output Formatting Examples

### Simple output
```basalt
"Hello, World!" print
```

### Multiple values on one line
```basalt
"The answer is: " . 42 print
```

### Building formatted output
```basalt
"Name: " . "Alice" . ", Age: " . 25 print
# Output: Name: Alice, Age: 25
```

### Spacing and newlines
```basalt
"Header" print
newline
"Content line 1" print
"Content line 2" print
newline
"Footer" print
```

**Output:**
```
Header

Content line 1
Content line 2

Footer
```

---

## Input Examples

### Number input
```basalt
"Enter first number: " . in
"Enter second number: " . in
+ print
```

### String concatenation with input
```basalt
"Enter your name: " . in
"Hello, " swap str+ print
```

### Conditional based on input
```basalt
"Enter 1 or 2: " . in
1 == { "You chose 1" print } { "You chose something else" print } if_jump
```

---

## Common Patterns

### Prompt and read
```basalt
"Enter value: " . in
```

### Print calculation
```basalt
5 10 + print    # Prints: 15
```

### Multi-line output
```basalt
"Line 1" print
"Line 2" print
"Line 3" print
```

### Inline formatting
```basalt
"Result: " . 100 print
```

### Blank line separator
```basalt
"Section 1" print
newline
"Section 2" print
```