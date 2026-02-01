# Popall

Completely clears the stack.

### **Stack Effect**
`( ... -- )`

### **Description**
`popall` (mapped to the `clear` function) removes every single item currently residing on the stack. It is a utility command used to reset the state of the interpreter.

* **Note:** This command does not trigger an underflow error if the stack is already empty; it simply ensures the stack remains empty.

### **Example**
```text
1 2 3 4 5 popall
# Stack logic: [1, 2, 3, 4, 5] -> []