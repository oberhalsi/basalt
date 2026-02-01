# Swap

Reverses the order of the top two items.

### **Stack Effect**
`( a b -- b a )`

### **Description**
`swap` takes the top two elements and exchanges their positions. This is critical for preparing arguments for operations where order matters, such as subtraction or division.

* **Underflow Protection:** Requires at least two items. If fewer are present, it triggers a `StackUnderflow` error: `"swap requires at least two items"`.

### **Example**
```text
2 10 swap / print
# Stack logic: [2, 10] -> [10, 2] -> [5]
# Output: 5