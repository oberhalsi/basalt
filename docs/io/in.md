### In

The `in` command reads a line of input from the user via the standard input stream and pushes it onto the stack.

### **Stack Effect**
`( -- value )`

### **Description**
When `in` is executed, the interpreter pauses and displays an input prompt (`> `). The user's response is captured and processed as follows:

1. **Numeric Conversion:** The interpreter first attempts to convert the input into an **integer**.
2. **String Fallback:** If the input cannot be parsed as an integer (contains letters or symbols), it is pushed onto the stack as a **string**.
3. **Empty Input:** If the user presses Enter without typing, an empty string is pushed.

---

### **Implementation Details**
The command utilizes Python's `input()` function. It includes built-in exception handling for:
* **EOFError:** Triggers a `Basalt Error: IOError` if the input stream is unexpectedly closed (e.g., `Ctrl+D`).
* **KeyboardInterrupt:** Gracefully handles `Ctrl+C` by notifying the user that input was cancelled.

### **Examples**

#### Reading an Integer
```text
in      # User types: 50
2 *
print   
# Output: 100