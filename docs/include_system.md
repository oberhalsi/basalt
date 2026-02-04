# Include System

## include (Import File)
**Stack Effect:** `filename --`

Loads and executes code from another Basalt file.

**Examples:**
```basalt
"std.b" include
"libs/math.b" include
"C:\path\to\file.b" include
```

**Errors:**
- StackUnderflow: If stack is empty
- TypeError: If filename is not a string
- FileNotFoundError: If file doesn't exist
- IOError: If file can't be read

**Important Notes:**
- Files are included relative to the current file's location
- Each file is only included once (circular import protection)
- Included code executes immediately
- Labels and variables from included files are available

---

## How Include Works

### 1. File Resolution
When you include a file, Basalt looks in this order:

1. **Relative to current file's directory**
2. Relative to current working directory  
3. Absolute path (if provided)

**Example:**
```
project/
├── main.b
├── lib.b
└── utils/
    └── helpers.b
```

**In main.b:**
```basalt
"lib.b" include           # Same directory
"utils/helpers.b" include # Subdirectory
```

**In utils/helpers.b:**
```basalt
"../lib.b" include        # Go up one directory
```

---

### 2. Execution
When a file is included:

1. File is read and tokenized
2. Tokens are inserted into the current program
3. Labels are registered
4. Code executes immediately

**Example:**

**lib.b:**
```basalt
"Loading library..." print
{ dup * } "square" =
```

**main.b:**
```basalt
"lib.b" include    # Prints "Loading library..." and defines square
5 "square" call run print    # → 25
```

---

### 3. Circular Import Protection
Each file can only be included once:

**a.b:**
```basalt
"b.b" include
"In a.b" print
```

**b.b:**
```basalt
"a.b" include    # Silently skipped (already included)
"In b.b" print
```

---

## Creating Library Files

### Simple Library
**math_lib.b:**
```basalt
# Math utility functions

{ dup * } "square" =
{ dup dup * * } "cube" =
{ 2 * } "double" =
{ 2 / } "half" =
```

**Using it:**
```basalt
"math_lib.b" include

5 "square" call run print    # → 25
3 "cube" call run print      # → 27
10 "double" call run print   # → 20
```

---

### Library with Dependencies
**advanced_math.b:**
```basalt
# Include basic math first
"math_lib.b" include

# Build on it
{ "square" call run "double" call run } "square_and_double" =
```

**Using it:**
```basalt
"advanced_math.b" include    # Also loads math_lib.b

5 "square_and_double" call run print    # → 50
```

---

## Standard Library Pattern

### Standard Library Structure
```
project/
├── main.b
├── std.b              # Core standard library
└── libs/
    ├── math.b         # Math utilities
    ├── string.b       # String utilities
    └── io.b           # I/O helpers
```

### std.b (Core Library)
```basalt
# Basalt Standard Library v1.0

# Math operations
{ dup * } "square" =
{ dup dup * * } "cube" =
{ 2 * } "double" =
{ 3 * } "triple" =

# Logic operations
{ 2 % 0 == } "is_even" =
{ 2 % 1 == } "is_odd" =

# I/O operations
{ print newline } "println" =
```

### Using Standard Library
```basalt
"std.b" include

5 "square" call run print
10 "is_even" call run print
"Hello!" "println" call run
```

---

## Common Patterns

### 1. Import Multiple Libraries
```basalt
"std.b" include
"libs/math.b" include
"libs/string.b" include

# Now use functions from all libraries
```

---

### 2. Conditional Include
```basalt
debug_mode
{ "debug_lib.b" include }
{ }
if_jump
```

---

### 3. Import at Top of File
```basalt
# Always import at the top
"std.b" include
"config.b" include

# Then your code
"Starting program..." print
```

---

### 4. Relative Imports
```basalt
# In utils/helper.b
"../std.b" include        # Go up one directory
"./local.b" include       # Same directory
```

---

## Best Practices

### 1. Library Files Should Only Define
**Good:**
```basalt
# math.b - Only definitions
{ dup * } "square" =
{ dup dup * * } "cube" =
```

**Bad:**
```basalt
# math.b - Has side effects
{ dup * } "square" =
"Loading math library..." print    # ❌ Prints every time
5 "square" call run print           # ❌ Executes code
```

---

### 2. Use Clear Naming
**Good:**
```basalt
"std.b" include
"math_utils.b" include
```

**Bad:**
```basalt
"lib.b" include
"util.b" include
```

---

### 3. Document Your Libraries
```basalt
# Math Utilities Library
# Provides common mathematical operations
#
# Functions:
#   square  - x -- x²
#   cube    - x -- x³
#   double  - x -- 2x

{ dup * } "square" =
{ dup dup * * } "cube" =
{ 2 * } "double" =
```

---

### 4. Group Related Functions
```basalt
# Good - one file per category
"math.b" include      # Math functions
"string.b" include    # String functions
"io.b" include        # I/O functions

# Bad - everything in one file
"everything.b" include
```

---

## Error Handling

### File Not Found
```basalt
"nonexistent.b" include
```

**Error:**
```
==================================================
Basalt Error: FileNotFoundError
==================================================
Command: 'include'
Message: Could not find file 'nonexistent.b'
==================================================
```

---

### Wrong Type
```basalt
123 include
```

**Error:**
```
==================================================
Basalt Error: TypeError
==================================================
Command: 'include'
Message: include expected a string filename, got int
==================================================
```

---

### Stack Underflow
```basalt
include
```

**Error:**
```
==================================================
Basalt Error: StackUnderflow
==================================================
Command: 'include'
Message: include requires a filename
==================================================
```

---

## Examples

### Example 1: Simple Program with Library
**lib.b:**
```basalt
{ dup * } "square" =
{ 2 * } "double" =
```

**main.b:**
```basalt
"lib.b" include

5 "square" call run "double" call run print    # → 50
```

---

### Example 2: Multi-File Project
**config.b:**
```basalt
100 "max_score" =
"MyApp" "app_name" =
```

**utils.b:**
```basalt
{ print newline } "println" =
```

**main.b:**
```basalt
"config.b" include
"utils.b" include

"app_name" call "println" call run
"Max score: " . "max_score" call print
```

---

### Example 3: Library with Dependencies
**basic.b:**
```basalt
{ 2 * } "double" =
```

**advanced.b:**
```basalt
"basic.b" include
{ "double" call run "double" call run } "quadruple" =
```

**main.b:**
```basalt
"advanced.b" include    # Also loads basic.b

5 "quadruple" call run print    # → 20
```

---

## Comparison with Other Languages

### Python
**Python:**
```python
import math
from utils import helper

result = math.sqrt(16)
```

**Basalt:**
```basalt
"math.b" include
"utils/helper.b" include

16 "sqrt" call run
```

---

### JavaScript
**JavaScript:**
```javascript
import { square, cube } from './math.js';

console.log(square(5));
```

**Basalt:**
```basalt
"math.b" include

5 "square" call run print
```

---

### C
**C:**
```c
#include "math.h"
#include "utils.h"

int result = square(5);
```

**Basalt:**
```basalt
"math.b" include
"utils.b" include

5 "square" call run
```

---

## Tips

1. **Always use strings** - `"file.b" include` not `file.b include`
2. **Include at top** - Make dependencies clear
3. **Relative paths** - Use `./ `and `../` for clarity
4. **Test libraries independently** - Make sure they work standalone
5. **Document what's exported** - List available functions in comments
6. **Keep libraries focused** - One purpose per file
7. **Use consistent naming** - `math.b` not `m.b` or `mathematics.b`

---

## Limitations

**Current limitations:**
- No namespace support (all variables are global)
- No selective imports (imports entire file)
- No import aliasing
- No lazy loading
- No module system

**Future enhancements could add:**
- `from "math.b" import "square" "cube"`
- `"math.b" as "m" include`
- Module namespaces
- Import control (public/private)
- Package management