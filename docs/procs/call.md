# Call

Retrieves a value from a variable and pushes it onto the stack.

### **Stack Effect**
`( name -- value )`

### **Description**
`call` pops a string from the stack, looks up that name in the global variable dictionary, and pushes the associated value back onto the stack.

* **NameError:** If the variable name has not been defined using `=`, the interpreter triggers a `NameError`.
* **Procedures:** When using procedures, `call` pushes the `{ }` block onto the stack, preparing it for the `run` command.

### **Example**
```text
{ 2 * } "double" =
5 "double" call 
# Stack now contains: 5, ['2', '*']