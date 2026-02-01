# Drop

Removes the top item from the stack.

### **Stack Effect**
`( a -- )`

### **Description**
`drop` removes (pops) the element currently at the top of the stack and discards it. This is used for "stack cleaning" once a value is no longer needed by your program.

* **Underflow Protection:** If the stack is empty, it triggers a `StackUnderflow` error: `"nothing to drop"`.

### **Example**
```text
10 20 drop print
# Stack logic: [10, 20] -> [10]
# Output: 10