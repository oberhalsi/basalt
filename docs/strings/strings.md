### **Strings in Basalt**
Strings are sequences of characters used for text output and data manipulation. 

#### **Syntax**
Strings are defined by enclosing text within double quotes (`"`).
* **Example:** `"Hello, Basalt!"`

#### **Internal Representation**
When the interpreter encounters a string, it is pushed onto the stack as a single unit. Unlike some low-level languages, a string in Basalt is not automatically treated as an array of characters unless specifically acted upon by a conversion command.

#### **String Behavior**
* **Printing:** When `print` or `.` is called on a string, the surrounding quotes are stripped, and the raw text is sent to the output.
* **Immutability:** Once a string is pushed to the stack, it is treated as a constant value. To "modify" a string, you would typically use operators to concatenate or slice them, pushing a new string result to the stack.

---

### **Example Usage**
```basalt
"Hello, " "World!" print