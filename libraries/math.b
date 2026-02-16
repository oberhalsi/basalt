# ============================================
# Basic Operations
# ============================================

{ dup * } "square" =
{ dup dup * * } "cube" =
{ 2 * } "double" =
{ 3 * } "triple" =
{ 2 / } "half" =

# ============================================
# Absolute Value & Sign
# ============================================

{
    dup 0 < "abs_neg" if_jump
    "abs_done" jump
abs_neg:
    0 swap -
abs_done:
} "abs" =

{
    dup 0 < "sign_neg" if_jump
    dup 0 > "sign_pos" if_jump
    drop 0
    "sign_done" jump
sign_neg:
    drop -1
    "sign_done" jump
sign_pos:
    drop 1
sign_done:
} "sign" =

{ 0 swap - } "negate" =

# ============================================
# Min/Max
# ============================================

{
    2 pick 2 pick < "min_first" if_jump
    swap drop
    "min_done" jump
min_first:
    drop
min_done:
} "min" =

{
    2 pick 2 pick > "max_first" if_jump
    swap drop
    "max_done" jump
max_first:
    drop
max_done:
} "max" =

# ============================================
# Checks
# ============================================

{ 2 % 0 == } "is_even" =
{ 2 % 1 == } "is_odd" =
{ % 0 == } "is_divisible" =

# ============================================
# Powers
# ============================================

{
    dup 0 == "p10_0" if_jump
    dup 1 == "p10_1" if_jump
    dup 2 == "p10_2" if_jump
    dup 3 == "p10_3" if_jump
    drop 10000
    "p10_done" jump
p10_0:
    drop 1
    "p10_done" jump
p10_1:
    drop 10
    "p10_done" jump
p10_2:
    drop 100
    "p10_done" jump
p10_3:
    drop 1000
p10_done:
} "pow10" =

# ============================================
# Factorial
# ============================================

{
    dup 0 == "f_0" if_jump
    dup 1 == "f_1" if_jump
    dup 2 == "f_2" if_jump
    dup 3 == "f_3" if_jump
    dup 4 == "f_4" if_jump
    dup 5 == "f_5" if_jump
    drop 720
    "f_done" jump
f_0:
f_1:
    drop 1
    "f_done" jump
f_2:
    drop 2
    "f_done" jump
f_3:
    drop 6
    "f_done" jump
f_4:
    drop 24
    "f_done" jump
f_5:
    drop 120
f_done:
} "factorial" =

# ============================================
# Simple Math
# ============================================

{ dup 1 + * 2 / } "sum_1_to_n" =
{ + 2 / } "average" =

# ============================================
# Range - NOW WITH LOCAL VARIABLES!
# ============================================

{
    "max_r" local        
    "min_r" local        
    dup min_r < not swap max_r > not and
} "in_range" =

{
    "max_c" local        
    "min_c" local        
    min_c max max_c min
} "clamp" =

# ============================================
# Digits
# ============================================

{
    dup abs
    dup 10 < "dc_1" if_jump
    dup 100 < "dc_2" if_jump
    dup 1000 < "dc_3" if_jump
    dup 10000 < "dc_4" if_jump
    drop 5
    "dc_done" jump
dc_1:
    drop 1
    "dc_done" jump
dc_2:
    drop 2
    "dc_done" jump
dc_3:
    drop 3
    "dc_done" jump
dc_4:
    drop 4
dc_done:
} "digits_count" =

# ============================================
# Utilities
# ============================================

{ 1 + } "inc" =
{ 1 - } "dec" =
{ square double } "square_and_double" =
{ cube half } "cube_and_half" =
