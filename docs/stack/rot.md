### **The `rot` (Rotate) Command**
`rot` takes the third element down on the stack and moves it to the top, shifting the other two elements down.

### **Stack Effect**
`( a b c -- b c a )`

* **Behavior:** It "rotates" the top three elements. The element that was at the bottom of the trio (`a`) becomes the new top element.
* **Use Case:** Essential for reordering data when you need to access a value buried under two other items without using temporary variables.

---

### **Example Usage**
**Stack before:** `[10, 20, 30]` (where 30 is the top)  
**Command:** `rot`  
**Stack after:** `[20, 30, 10]`