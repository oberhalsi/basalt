# Run

Executes a code block (quotation) popped from the stack.

### **Stack Effect**
`( [block] -- ? )`

### **Description**
`run` is the engine for procedures in Basalt. It pops a list (quotation) from the top of the stack and executes its tokens recursively within the current environment.

* **StackUnderflow:** Triggers an error if the stack is empty when `run` is called.
* **Context Preservation:** Jumps and labels are shared with the parent execution context to allow for complex control flow within blocks.

### **Example**
```text
{ dup * } "square" =
5 "square" call run print
# Output: 25