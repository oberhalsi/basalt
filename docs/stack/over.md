### **The `over` Command**
`over` copies the second element on the stack and pushes it to the top.

### **Stack Effect**
`( a b -- a b a )`

* **Behavior:** It "reaches over" the top element to grab a copy of the one beneath it.
* **Use Case:** Useful when you have two values and you need to perform an operation on them while still keeping both original values available for later.

---

### **Example Usage**
**Stack before:** `[10, 20]` (where 20 is the top)  
**Command:** `over`  
**Stack after:** `[10, 20, 10]`