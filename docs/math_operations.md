# Math Operations

## + (Addition)
**Stack Effect:** `a b -- (a+b)`

Adds two numbers together.

**Examples:**
```basalt
5 10 +        # → 15
-3 7 +        # → 4
100 50 +      # → 150
```

**Errors:**
- StackUnderflow: If fewer than 2 values on stack
- TypeError: If trying to add incompatible types (e.g., string + number)

---

## - (Subtraction)
**Stack Effect:** `a b -- (a-b)`

Subtracts b from a.

**Examples:**
```basalt
10 3 -        # → 7
5 10 -        # → -5
0 5 -         # → -5
```

**Errors:**
- StackUnderflow: If fewer than 2 values on stack
- TypeError: If trying to subtract incompatible types

---

## * (Multiplication)
**Stack Effect:** `a b -- (a*b)`

Multiplies two numbers.

**Examples:**
```basalt
5 6 *         # → 30
-3 4 *        # → -12
10 10 *       # → 100
```

**Errors:**
- StackUnderflow: If fewer than 2 values on stack
- TypeError: If trying to multiply incompatible types

---

## / (Division)
**Stack Effect:** `a b -- (a/b)`

Integer division (floors the result).

**Examples:**
```basalt
10 2 /        # → 5
10 3 /        # → 3 (floors)
15 4 /        # → 3
```

**Errors:**
- StackUnderflow: If fewer than 2 values on stack
- MathError: Division by zero
- TypeError: If trying to divide incompatible types

**Notes:**
- On division by zero, the values are pushed back to preserve stack state

---

## % (Modulo)
**Stack Effect:** `a b -- (a%b)`

Returns remainder of a divided by b.

**Examples:**
```basalt
10 3 %        # → 1
17 5 %        # → 2
20 4 %        # → 0
```

**Errors:**
- StackUnderflow: If fewer than 2 values on stack
- MathError: Modulo by zero

---

## ^ (Power)
**Stack Effect:** `base exponent -- (base^exponent)`

Raises base to the power of exponent.

**Examples:**
```basalt
2 3 ^         # → 8
5 2 ^         # → 25
2 10 ^        # → 1024
10 0 ^        # → 1
```

**Errors:**
- StackUnderflow: If fewer than 2 values on stack
- MathError: Zero to negative power
- MathError: Result too large (overflow)

---

## Common Patterns

### Square a number
```basalt
5 dup *       # 5² = 25
```

### Cube a number
```basalt
5 dup dup * * # 5³ = 125
```

### Average of two numbers
```basalt
10 20 + 2 /   # (10+20)/2 = 15
```

### Absolute value
```basalt
-5 dup 0 < { 0 swap - } { } if_jump  # → 5
```