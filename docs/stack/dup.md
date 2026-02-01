# Dup

Duplicates the top item on the stack.

### **Stack Effect**
`( a -- a a )`

### **Description**
`dup` (duplicate) takes the value at the top of the stack and pushes an identical copy on top of it. This is the primary way to use a value in a calculation while preserving it for later use.

* **Underflow Protection:** If the stack is empty, it triggers a `StackUnderflow` error: `"nothing to duplicate"`.

### **Example**
```text
5 dup * print
# Stack logic: [5] -> [5, 5] -> [25]
# Output: 25