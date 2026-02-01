# = (Assign)

Assigns a value or a code block to a named variable.

### **Stack Effect**
`( value name -- )`

### **Description**
The `=` operator pops a name (string) and a value from the stack and stores them in the internal global dictionary. In Basalt, variables are dynamic: you can store integers, strings, or even code blocks (quotations).

* **Underflow Protection:** Requires a value and a name.
* **Overwriting:** If the variable name already exists, the old value is replaced with the new one.

### **Example**
```text
10 "age" =
"age" call print
# Output: 10