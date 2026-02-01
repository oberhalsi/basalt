# Print

The `print` command writes the top of the stack into the standard output stream.

### **Stack Effect**
`( a -- )`

### **Description**
`print` pops the top element from the stack and converts it to a string representation before sending it to the output.

* **Integers:** Rendered as standard base-10 numerals.
* **Strings:** Rendered as raw text (quotes are stripped).
* **Quotations (Blocks):** Rendered in their internal list format (e.g., `['dup', '*']`), which is essential for inspecting procedures.

After the value is emitted, a **newline character** is automatically appended to the stream.

---

### **Implementation Details**
In the Basalt CPython-based interpreter, this operator checks for stack depth before execution. If the stack contains fewer than **1** item, it triggers a `StackUnderflow` error through the `Error()` utility.

### **Examples**

#### Basic Output
```text
42 print
# Output: 42