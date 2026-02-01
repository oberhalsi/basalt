## Comparison Operations

This module provides stack-based comparison logic. Each function expects a list (`stack`) as input and performs operations by popping the top two values and pushing the result (1 for true, 0 for false).

---

### Functions

#### `==`
Compares the top two values for equality.
* **Stack Effect**: `[..., a, b] -> [..., result]`
* **Errors**: 
  * `StackUnderflow`: Raised if `len(stack) < 2`.
* **Logic**: Pushes `1` if `a == b`, else `0`.

#### `>`
Checks if the second element from the top is greater than the top element.
* **Stack Effect**: `[..., a, b] -> [..., result]`
* **Errors**: 
  * `StackUnderflow`: Raised if `len(stack) < 2`.
  * `TypeError`: Raised if `a` and `b` cannot be compared (e.g., `int` vs `str`).
* **Logic**: Pushes `1` if `a > b`, else `0`.

#### `<`
Checks if the second element from the top is less than the top element.
* **Stack Effect**: `[..., a, b] -> [..., result]`
* **Errors**: 
  * `StackUnderflow`: Raised if `len(stack) < 2`.
  * `TypeError`: Raised if `a` and `b` cannot be compared.
* **Logic**: Pushes `1` if `a < b`, else `0`.

