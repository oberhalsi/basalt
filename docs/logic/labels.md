# Control Flow: Labels and Jumps

Labels are how you navigate your code. Since this language is stack-based, you don't have standard `if/else` blocks or `while` loops. Instead, you use **Labels** as anchors and **Jumps** to move between them.

---

## 1. Creating an Anchor (Labels)
To mark a spot in your code that you want to return to or skip to, use a colon `:` at the end of a word.

**Syntax:** `name:`

* Labels do not interact with the stack.
* They act as "bookmarks" for the interpreter.
* **Example:** `start_loop:` or `on_error:`

---

## 2. Moving Around (Jumps)
There are two ways to move the execution to a label. Both require you to push the label's name onto the stack as a **string** (using double quotes).

### The Unconditional Jump (`jump`)
This is a direct "Go To" command. 
* **Stack**: Requires a label name string at the top.
* **Example**: `"top" jump` — This immediately sends the program back to `top:`.

### The Conditional Jump (`if_jump`)
This is how you handle logic. It only jumps if the value below the label name is "true" (non-zero).
* **Stack**: `[condition, "label_name"]`
* **Example**: 
  ```text
  x 10 > "target" if_jump