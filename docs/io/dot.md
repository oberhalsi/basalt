### **The `.` (Dot) Command**
`.` pops the top element from the stack and converts it to a string representation for the output **without** adding a newline.

### **Stack Effect**
`( a -- )`

* **Integers:** Rendered as standard base-10 numerals.
* **Strings:** Rendered as raw text (quotes are stripped).
* **Quotations (Blocks):** Rendered in their internal list format (e.g., `['dup', '*']`).

Unlike `print`, this command does not append a newline character to the output stream, allowing for consecutive values to be displayed on the same line.