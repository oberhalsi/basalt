# Logic Operations

## == (Equal)
**Stack Effect:** `a b -- bool`

Returns 1 if equal, 0 otherwise.

**Examples:**
```basalt
5 5 ==          # → 1 (true)
5 10 ==         # → 0 (false)
"hi" "hi" ==    # → 1 (true)
"hi" "bye" ==   # → 0 (false)
```

**Errors:**
- StackUnderflow: If fewer than 2 values on stack

**Common Uses:**
```basalt
# Check if zero
10 0 == { "Zero!" print } { "Not zero" print } if_jump

# Compare strings
"yes" "yes" == print    # → 1
```

---

## > (Greater Than)
**Stack Effect:** `a b -- bool`

Returns 1 if a > b, 0 otherwise.

**Examples:**
```basalt
10 5 >          # → 1 (true)
5 10 >          # → 0 (false)
5 5 >           # → 0 (false)
```

**Errors:**
- StackUnderflow: If fewer than 2 values on stack
- TypeError: Cannot compare string and number

**Common Uses:**
```basalt
# Check if positive
10 0 > { "Positive" print } { "Not positive" print } if_jump

# Find max
10 20 2 pick 2 pick > { drop } { swap drop } if_jump
```

---

## < (Less Than)
**Stack Effect:** `a b -- bool`

Returns 1 if a < b, 0 otherwise.

**Examples:**
```basalt
5 10 <          # → 1 (true)
10 5 <          # → 0 (false)
5 5 <           # → 0 (false)
```

**Errors:**
- StackUnderflow: If fewer than 2 values on stack
- TypeError: Cannot compare string and number

**Common Uses:**
```basalt
# Check if negative
-5 0 < { "Negative" print } { "Not negative" print } if_jump

# Find min
10 20 2 pick 2 pick < { drop } { swap drop } if_jump
```

---

## and (Logical AND)
**Stack Effect:** `a b -- bool`

Returns 1 if both a and b are truthy, 0 otherwise.

**Examples:**
```basalt
1 1 and         # → 1 (true)
1 0 and         # → 0 (false)
0 0 and         # → 0 (false)
5 10 and        # → 1 (both non-zero)
```

**Errors:**
- StackUnderflow: If fewer than 2 values on stack

**Common Uses:**
```basalt
# Check range: 0 < x < 100
50 0 > swap 100 < and

# Multiple conditions
age 18 > employed and
```

---

## or (Logical OR)
**Stack Effect:** `a b -- bool`

Returns 1 if either a or b (or both) are truthy, 0 otherwise.

**Examples:**
```basalt
1 0 or          # → 1 (true)
0 1 or          # → 1 (true)
0 0 or          # → 0 (false)
5 0 or          # → 1 (true)
```

**Errors:**
- StackUnderflow: If fewer than 2 values on stack

**Common Uses:**
```basalt
# Check if outside range
x 0 < x 100 > or

# Either condition
is_admin is_moderator or
```

---

## not (Logical NOT)
**Stack Effect:** `a -- bool`

Returns 1 if a is falsy (0 or empty), 0 if a is truthy.

**Examples:**
```basalt
0 not           # → 1 (true)
1 not           # → 0 (false)
5 not           # → 0 (false)
```

**Errors:**
- StackUnderflow: If stack is empty

**Common Uses:**
```basalt
# Invert condition
is_valid not { "Invalid!" print } { } if_jump

# Check if zero
value not { "Value is zero" print } { } if_jump
```

---

## xor (Logical XOR)
**Stack Effect:** `a b -- bool`

Returns 1 if exactly one of a or b is truthy, 0 otherwise.

**Examples:**
```basalt
1 0 xor         # → 1 (true)
0 1 xor         # → 1 (true)
1 1 xor         # → 0 (false)
0 0 xor         # → 0 (false)
```

**Errors:**
- StackUnderflow: If fewer than 2 values on stack

**Common Uses:**
```basalt
# Exclusive or
has_password has_token xor { "Use one auth method only" print } { } if_jump
```

---

## Truthiness in Basalt

**Truthy values:**
- Any non-zero number: 1, 5, -3, 100
- Any non-empty string: "hello", "0", "false"
- Any code block: { ... }

**Falsy values:**
- Zero: 0
- Empty string: "" (though harder to create)

---

## Common Patterns

### Check if in range (0 < x < 100)
```basalt
x 0 > x 100 < and
```

### Check if outside range (x < 0 OR x > 100)
```basalt
x 0 < x 100 > or
```

### Check if even
```basalt
x 2 % 0 ==
```

### Check if odd
```basalt
x 2 % 1 ==
```

### Check if positive
```basalt
x 0 >
```

### Check if negative
```basalt
x 0 <
```

### Check if zero
```basalt
x 0 ==
```

### Check if non-zero
```basalt
x 0 == not
```

### Multiple AND conditions
```basalt
cond1 cond2 and cond3 and
```

### Multiple OR conditions
```basalt
cond1 cond2 or cond3 or
```

---

## Comparison Chain Examples

### Age verification (18 <= age <= 65)
```basalt
age 18 >= age 65 <= and
{ "Valid age" print }
{ "Invalid age" print }
if_jump
```

### Grade classification
```basalt
# If score >= 90: "A"
score 90 >=
{ "Grade: A" print }
{
    # Else if score >= 80: "B"
    score 80 >=
    { "Grade: B" print }
    { "Grade: C or below" print }
    if_jump
}
if_jump
```

### Multiple conditions
```basalt
# Must be: adult AND (employed OR student)
age 18 > 
employed student or 
and
{ "Approved" print }
{ "Denied" print }
if_jump
```