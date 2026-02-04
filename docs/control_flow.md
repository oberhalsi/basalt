# Control Flow

## Labels
**Syntax:** `label_name:`

Defines a label at a specific point in the program.

**Examples:**
```basalt
start:
    "Hello" print
    "start" jump    # Infinite loop
```

**Important Notes:**
- Labels end with a colon `:`
- Labels don't consume stack values
- Labels can be jumped to from anywhere
- Multiple labels can exist in a program

---

## jump (Unconditional Jump)
**Stack Effect:** `label_name --`

Jumps to the specified label unconditionally.

**Examples:**
```basalt
"skip" jump
"This won't print" print
skip:
"This will print" print
```

**Errors:**
- StackUnderflow: If stack is empty
- TypeError: If label is not a string
- NameError: If label doesn't exist

**Common Uses:**
```basalt
# Skip code
"end" jump
"Skipped" print
end:

# Loop
loop:
    "Hello" print
    "loop" jump
```

---

## if_jump (Conditional Jump)
**Stack Effect:** `condition label_name --`

Jumps to the specified label if the condition is truthy (non-zero).

**Examples:**
```basalt
1 "yes" if_jump
"Condition was false" print
yes:
"Condition was true" print
```

**Errors:**
- StackUnderflow: If fewer than 2 values on stack
- TypeError: If label is not a string
- NameError: If label doesn't exist

**Common Uses:**
```basalt
# If-then
age 18 > "adult" if_jump
"You are a minor" print
adult:

# If-else pattern
age 18 > "adult" if_jump
"You are a minor" print
"done" jump
adult:
"You are an adult" print
done:
```

---

## Control Flow Patterns

### 1. If-Then (Execute if true)
```basalt
x 0 > "positive" if_jump
"done" jump

positive:
    "Number is positive" print

done:
```

---

### 2. If-Else (Execute one branch)
```basalt
x 0 > "positive" if_jump

# Else branch
"Number is not positive" print
"done" jump

positive:
    "Number is positive" print

done:
```

---

### 3. If-Else-If Chain
```basalt
score 90 >= "grade_a" if_jump
score 80 >= "grade_b" if_jump
score 70 >= "grade_c" if_jump

# Default case
"Grade: F" print
"done" jump

grade_a:
    "Grade: A" print
    "done" jump

grade_b:
    "Grade: B" print
    "done" jump

grade_c:
    "Grade: C" print

done:
```

---

### 4. Loops - While Loop
```basalt
0 "counter" =

loop:
    "counter" call 10 < "continue" if_jump
    "done" jump
    
continue:
    "counter" call print
    "counter" call 1 + "counter" =
    "loop" jump

done:
```

---

### 5. Loops - Infinite Loop with Break
```basalt
loop:
    "Enter 0 to quit: " . in
    dup 0 == "break" if_jump
    
    "You entered: " . print
    "loop" jump

break:
    drop
    "Goodbye!" print
```

---

### 6. Counted Loop (For Loop)
```basalt
0 "i" =

for_loop:
    "i" call 5 < "continue" if_jump
    "done" jump

continue:
    "Iteration: " . "i" call print
    "i" call 1 + "i" =
    "for_loop" jump

done:
```

---

### 7. Do-While Loop (Execute at least once)
```basalt
do:
    "Enter number: " . in
    dup print
    
    0 > "do" if_jump
    
"Loop ended" print
```

---

## Advanced Patterns

### 1. Nested If Statements
```basalt
x 0 > "check_range" if_jump
"Number must be positive" print
"done" jump

check_range:
    x 100 < "valid" if_jump
    "Number too large" print
    "done" jump

valid:
    "Number is valid" print

done:
```

---

### 2. Switch-Case Pattern
```basalt
# Get choice
choice "input_choice" =

"input_choice" call 1 == "case_1" if_jump
"input_choice" call 2 == "case_2" if_jump
"input_choice" call 3 == "case_3" if_jump

# Default case
"Invalid choice" print
"done" jump

case_1:
    "You chose 1" print
    "done" jump

case_2:
    "You chose 2" print
    "done" jump

case_3:
    "You chose 3" print

done:
```

---

### 3. Menu Loop
```basalt
menu:
    "1. Option 1" print
    "2. Option 2" print
    "3. Exit" print
    "Choice: " . in
    
    dup 1 == "option1" if_jump
    dup 2 == "option2" if_jump
    dup 3 == "exit" if_jump
    
    drop
    "Invalid choice" print
    "menu" jump

option1:
    drop
    "Option 1 selected" print
    "menu" jump

option2:
    drop
    "Option 2 selected" print
    "menu" jump

exit:
    drop
    "Goodbye!" print
```

---

### 4. Early Exit Pattern
```basalt
# Check precondition 1
valid1 not "error" if_jump

# Check precondition 2
valid2 not "error" if_jump

# Main logic
"All checks passed" print
"done" jump

error:
    "Error: validation failed" print

done:
```

---

### 5. Guard Clauses
```basalt
# Guard: must be positive
value 0 <= "invalid" if_jump

# Guard: must be less than 100
value 100 >= "invalid" if_jump

# Main logic
"Value is valid" print
"done" jump

invalid:
    "Invalid value" print

done:
```

---

## Comparison with Other Languages

### If Statement
**Python:**
```python
if x > 0:
    print("Positive")
```

**Basalt:**
```basalt
x 0 > "positive" if_jump
"done" jump

positive:
    "Positive" print

done:
```

---

### If-Else Statement
**Python:**
```python
if x > 0:
    print("Positive")
else:
    print("Not positive")
```

**Basalt:**
```basalt
x 0 > "positive" if_jump

"Not positive" print
"done" jump

positive:
    "Positive" print

done:
```

---

### While Loop
**Python:**
```python
i = 0
while i < 10:
    print(i)
    i += 1
```

**Basalt:**
```basalt
0 "i" =

loop:
    "i" call 10 < "continue" if_jump
    "done" jump

continue:
    "i" call print
    "i" call 1 + "i" =
    "loop" jump

done:
```

---

### For Loop
**Python:**
```python
for i in range(5):
    print(i)
```

**Basalt:**
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

## Common Pitfalls

### 1. Forgetting End Label
```basalt
# Bad - infinite loop
x 0 > "positive" if_jump
"Not positive" print

positive:
    "Positive" print
    # Falls through and loops!
```

```basalt
# Good - explicit end
x 0 > "positive" if_jump
"Not positive" print
"done" jump

positive:
    "Positive" print

done:
```

---

### 2. Wrong Stack Order for if_jump
```basalt
# Bad - label on top, condition below
"label" condition if_jump

# Good - condition on top, label below
condition "label" if_jump
```

---

### 3. Using Number as Label
```basalt
# Bad
123 if_jump    # ERROR: label must be string

# Good
"label_123" if_jump
```

---

## Best Practices

### 1. Use Descriptive Label Names
```basalt
# Good
"error_handler" if_jump
"main_loop" jump

# Bad
"a" if_jump
"x" jump
```

---

### 2. Always Have an Exit
```basalt
# Good - has exit condition
loop:
    condition "done" if_jump
    "loop" jump
done:

# Bad - infinite loop
loop:
    "loop" jump
```

---

### 3. Structure Your Code
```basalt
# Good - clear structure
main:
    # Main logic
    "helper" jump

helper:
    # Helper logic
    "done" jump

done:
    # Exit
```

---

### 4. Comment Complex Flow
```basalt
# Calculate factorial
1 "result" =
n "counter" =

loop:
    # Exit if counter reaches 0
    "counter" call 0 == "done" if_jump
    
    # result = result * counter
    "result" call "counter" call * "result" =
    
    # counter = counter - 1
    "counter" call 1 - "counter" =
    
    "loop" jump

done:
    "result" call print
```

---

## Tips

1. **Use meaningful label names** - Makes code readable
2. **Always provide exit conditions** - Prevent infinite loops
3. **Structure with consistent indentation** - Improves readability
4. **Test edge cases** - Especially loop boundaries
5. **Keep control flow simple** - Easier to understand and debug