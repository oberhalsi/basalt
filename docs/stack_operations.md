# Stack Operations

## dup (Duplicate)
**Stack Effect:** `a -- a a`

Duplicates the top value on the stack.

**Examples:**
```basalt
5 dup           # Stack: [5, 5]
"Hello" dup     # Stack: ["Hello", "Hello"]
```

**Errors:**
- StackUnderflow: If stack is empty

**Common Uses:**
```basalt
5 dup *         # Square a number (5 * 5 = 25)
10 dup print    # Print and keep value
```

---

## drop (Drop)
**Stack Effect:** `a --`

Removes the top value from the stack.

**Examples:**
```basalt
5 10 drop       # Stack: [5]
1 2 3 drop drop # Stack: [1]
```

**Errors:**
- StackUnderflow: If stack is empty

**Common Uses:**
```basalt
5 10 20 drop    # Discard unwanted value
```

---

## swap (Swap)
**Stack Effect:** `a b -- b a`

Swaps the top two values on the stack.

**Examples:**
```basalt
5 10 swap       # Stack: [10, 5]
"A" "B" swap    # Stack: ["B", "A"]
```

**Errors:**
- StackUnderflow: If fewer than 2 values on stack

**Common Uses:**
```basalt
10 3 swap /     # 3 / 10 instead of 10 / 3
5 10 swap -     # 10 - 5 instead of 5 - 10
```

---

## over (Over)
**Stack Effect:** `a b -- a b a`

Copies the second value to the top.

**Examples:**
```basalt
5 10 over       # Stack: [5, 10, 5]
1 2 over        # Stack: [1, 2, 1]
```

**Errors:**
- StackUnderflow: If fewer than 2 values on stack

**Common Uses:**
```basalt
5 10 over + +   # 5 + 10 + 5 = 20
```

---

## rot (Rotate)
**Stack Effect:** `a b c -- b c a`

Rotates the third item to the top.

**Examples:**
```basalt
1 2 3 rot       # Stack: [2, 3, 1]
5 10 15 rot     # Stack: [10, 15, 5]
```

**Errors:**
- StackUnderflow: If fewer than 3 values on stack

**Common Uses:**
```basalt
# Rearrange three values
1 2 3 rot       # Move 1 to top
```

---

## pick (Pick)
**Stack Effect:** `... n -- ... (nth item)`

Copies the nth item from the stack to the top (1-indexed from top).

**Examples:**
```basalt
10 20 30 2 pick     # Stack: [10, 20, 30, 20]
1 2 3 4 3 pick      # Stack: [1, 2, 3, 4, 2]
```

**Errors:**
- StackUnderflow: If stack too shallow for n
- StackUnderflow: If stack is empty

**Common Uses:**
```basalt
# Access deep stack values
5 10 15 20 4 pick   # Gets 5 from bottom
```

---

## popall (Clear)
**Stack Effect:** `... --`

Clears the entire stack.

**Examples:**
```basalt
1 2 3 4 5 popall    # Stack: []
```

**Common Uses:**
```basalt
# Clean slate
5 10 15 20 popall
"Starting fresh" print
```

---

## Stack Visualization Examples

### Basic stack manipulation
```basalt
# Start: []
5               # [5]
10              # [5, 10]
dup             # [5, 10, 10]
swap            # [5, 10, 10]
drop            # [5, 10]
```

### Complex example
```basalt
# Calculate: (a + b) * (a - b)
# Where a=5, b=3

5 3             # [5, 3]
2 pick          # [5, 3, 5]
2 pick          # [5, 3, 5, 3]
-               # [5, 3, 2]
rot             # [3, 2, 5]
rot             # [2, 5, 3]
+               # [2, 8]
*               # [16]
```

---

## Common Patterns

### Keep a value while using it
```basalt
10 dup print    # Prints 10, keeps 10 on stack
```

### Swap for correct order
```basalt
"World" "Hello" swap str+  # "Hello" + "World"
```

### Copy deep values
```basalt
1 2 3 4 5 5 pick    # Gets the 1
```

### Clean up stack
```basalt
1 2 3 4 5 popall    # Remove everything
```