# Arithmetic Operators

Arithmetic in Basalt follows the **Postfix (Reverse Polish Notation)** system. Operators pop the required number of operands from the top of the stack and push the result back.

### **Safety Features**
Unlike many low-level languages, Basalt includes built-in safety checks for all arithmetic operations:

* **Underflow Protection:** Every operator verifies that at least two items exist on the stack before attempting to pop.
* **Type Validation:** If you attempt to perform math on incompatible types (e.g., adding an integer to a string), a `TypeError` is triggered.
* **Data Preservation:** In the event of a `MathError` (like Division by Zero), the interpreter attempts to preserve the stack state where possible to prevent data loss.

---

### **Operator Summary**

| Operator | Name | Effect | Technical Note |
| :--- | :--- | :--- | :--- |
| `+` | Addition | `( a b -- sum )` | Supports integer addition and string concatenation. |
| `-` | Subtraction | `( a b -- diff )` | Calculates `a - b`. |
| `*` | Multiplication | `( a b -- prod )` | Supports integer multiplication and string repetition. |
| `/` | Integer Division | `( a b -- quot )` | Uses floor division (`//`). Division by zero is protected. |
| `%` | Modulo | `( a b -- rem )` | Returns the remainder of `a / b`. |

---

### **Order of Operations**
In Basalt, the **top** of the stack is the second operand (`b`), and the **second-to-top** is the first operand (`a`).

```text
10 2 / print
# a=10, b=2
# Output: 5