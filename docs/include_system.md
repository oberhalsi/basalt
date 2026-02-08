# Include System

## include (Import File)
**Stack Effect:** `filename --`

Loads and executes code from another Basalt file.

**Examples:**
```basalt
"math" include              # Standard library from libraries/ folder
"utils/helper.b" include    # Relative path
"C:\path\to\file.b" include # Absolute path
```

**Errors:**
- StackUnderflow: If stack is empty
- TypeError: If filename is not a string
- FileNotFoundError: If file doesn't exist in libraries/ or as path
- IOError: If file can't be read

**Important Notes:**
- Files are included relative to the current file's location
- Each file is only included once (circular import protection)
- Included code executes immediately
- Labels and variables from included files are available
- `.b` extension is automatically added if not present

---

## How Include Works

### 1. File Resolution (Library Search Path)
When you include a file, Basalt searches in this order:

1. **Standard library folder** (`libraries/`)
2. **Relative to current file's directory**
3. **Relative to current working directory**
4. **Absolute path** (if provided)

**Example:**
```
project/
├── main.b
├── libraries/
│   ├── math.b
│   └── rng.b
└── utils/
    └── helpers.b
```

**In main.b:**
```basalt
"math" include              # Finds libraries/math.b
"rng" include               # Finds libraries/rng.b
"utils/helpers.b" include   # Relative path
```

**In utils/helpers.b:**
```basalt
"math" include              # Still finds libraries/math.b
"../main.b" include         # Relative to helpers.b location
```

---

### 2. Automatic .b Extension
The `.b` extension is optional:

```basalt
"math" include       # Searches for math.b
"math.b" include     # Also works
```

Both find `libraries/math.b`.

---

### 3. Execution
When a file is included:

1. File is searched in library paths
2. File is read and tokenized
3. Tokens are inserted into the current program
4. Labels are registered
5. Code executes immediately

**Example:**

**libraries/math.b:**
```basalt
{ dup * } "square" =
{ dup dup * * } "cube" =
```

**main.b:**
```basalt
"math" include    # Loads from libraries/
5 square print    # → 25 (no "call run" needed!)
```

---

### 4. Circular Import Protection
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

## Standard Library

### Using Standard Libraries
Standard libraries are in the `libraries/` folder and can be imported by name:

```basalt
"math" include     # libraries/math.b
"rng" include      # libraries/rng.b
```

### Available Standard Libraries
- **math.b** - Mathematical functions (square, cube, abs, min, max, factorial, pow10, sum_1_to_n, average, in_range, clamp, digits_count, etc.)
- **rng.b** - Random number generation

---

## Creating Library Files

### Simple Library
**libraries/mylib.b:**
```basalt
# My utility functions

{ dup * } "square" =
{ dup dup * * } "cube" =
{ 2 * } "double" =
{ 2 / } "half" =
```

**Using it:**
```basalt
"mylib" include

5 square print    # → 25
3 cube print      # → 27
10 double print   # → 20
```

---

### Library with Dependencies
**libraries/advanced_math.b:**
```basalt
# Include basic math first
"math" include

# Build on it
{ square double } "square_and_double" =
```

**Using it:**
```basalt
"advanced_math" include    # Also loads math

5 square_and_double print    # → 50
```

---

## Common Patterns

### 1. Import Multiple Libraries
```basalt
"math" include
"rng" include

# Use functions from both
1 10 rand print
5 square print
```

---

### 2. Import at Top of File
```basalt
# Always import at the top
"math" include

# Then your code
"Starting program..." print
5 square print
```

---

### 3. Custom Library Paths
For files not in `libraries/`:

```basalt
"../myproject/utils.b" include    # Relative path
"C:\libs\custom.b" include         # Absolute path
```

---

## Best Practices

### 1. Library Files Should Only Define Functions
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
5 square print                      # ❌ Executes code on import
```

---

### 2. Use Standard Library for Common Code
Put reusable functions in `libraries/` so they can be imported by name:

```basalt
"math" include      # ✅ Clear and simple
"libraries/math.b" include    # ❌ Redundant
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

### 4. One Purpose Per Library
```basalt
# Good - focused libraries
"math" include      # Math functions
"string" include    # String functions
"io" include        # I/O helpers

# Bad - everything in one
"everything" include
```

---

## Error Handling

### File Not Found
```basalt
"nonexistent" include
```

**Error:**
```
==================================================
Basalt Error: FileNotFoundError
==================================================
Command: 'include'
Message: Could not find file 'nonexistent' in libraries/ or as a path
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

### Example 1: Using Standard Library
```basalt
"math" include

5 square print        # → 25
-10 abs print         # → 10
3 factorial print     # → 6
10 20 min print       # → 10
```

---

### Example 2: Multi-File Project
**config.b:**
```basalt
100 "max_score" =
"MyApp" "app_name" =
```

**main.b:**
```basalt
"math" include
"config.b" include

app_name print
"Max score: " . max_score print
5 square print
```

---

### Example 3: Library Chain
**libraries/basic.b:**
```basalt
{ 2 * } "double" =
```

**libraries/advanced.b:**
```basalt
"basic" include
{ double double } "quadruple" =
```

**main.b:**
```basalt
"advanced" include    # Also loads basic

5 quadruple print    # → 20
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
"math" include

5 square print
```

---

### JavaScript/Node.js
**JavaScript:**
```javascript
const math = require('./math');
const utils = require('utils');

console.log(math.square(5));
```

**Basalt:**
```basalt
"math" include

5 square print
```

---

### C
**C:**
```c
#include <math.h>      // System library
#include "mylib.h"     // Local library
```

**Basalt:**
```basalt
"math" include         # Standard library
"mylib.b" include      # Custom library
```

---

## Library Search Path Details

The search path works like Python's `sys.path`:

1. **`libraries/`** - Standard library location (always checked first)
2. **Current file's directory** - For relative imports
3. **Current working directory** - Where you ran the program

This means:
- Standard libraries are globally accessible by name
- Custom libraries need paths (relative or absolute)
- The system is smart about finding files

---

## Tips

1. **Use library names for standard libs** - `"math" include` not `"libraries/math.b" include`
2. **Include at top** - Make dependencies clear
3. **Relative paths for custom code** - `"utils/helper.b" include`
4. **Test libraries independently** - Make sure they work standalone
5. **Document exported functions** - List available functions in comments
6. **Keep libraries focused** - One purpose per file
7. **Extension is optional** - `"math"` and `"math.b"` both work

---

## Limitations

**Current limitations:**
- No namespace support (all variables are global)
- No selective imports (imports entire file)
- No import aliasing
- No lazy loading
- No private/public functions

**Future enhancements could add:**
- `from "math" import square cube`
- `"math" as m include`
- Module namespaces
- Private functions (prefix with `_`)
- Package manager