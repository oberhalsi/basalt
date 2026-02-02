### **Logic Gate Operators**

In programming, logic gates are typically represented by two types of operators: **Bitwise** (operating on individual bits) and **Logical** (operating on true/false values). In this system, `1` represents **True** and `0` represents **False**.

#### **Logical Operators**
Used for conditional branching and boolean logic.

| Gate | Keyword | Description |
| :--- | :--- | :--- |
| **AND** | `and` | Returns 1 if both inputs are 1. |
| **OR** | `or` | Returns 1 if at least one input is 1. |
| **NOT** | `not` | Reverses the logic (1 becomes 0, 0 becomes 1). |
| **XOR** | `xor` | Returns 1 if the inputs are different (e.g., 1 and 0). |

---

### **Implementation Logic (1 = True, 0 = False)**
When implementing these in your interpreter, you can treat any non-zero integer as `1` for the input, but ensuring the output is strictly `1` or `0` keeps the stack clean for future operations.