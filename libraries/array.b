# Array Library for Basalt
# Arrays implemented using dynamic variable names

"math" include

# ============================================
# Core Array Operations
# ============================================

{
    "arr_name" local
    "idx" local
    "val" local
  
    "__arr_" arr_name str+ "_" str+ idx int_to_str str+ "varname" local
    
    val varname set_dynamic
} "array_set" =

{
    "arr_name" local
    "idx" local
    
    "__arr_" arr_name str+ "_" str+ idx int_to_str str+ "varname" local
    
    varname get_dynamic
} "array_get" =

{
    "arr_name" local
    "size" local
    0 "i" local
    
init_loop:
    i size < "init_continue" if_jump
    "init_done" jump
    
init_continue:
    0 i arr_name array_set
    i inc "i" local
    "init_loop" jump
    
init_done:
} "array_new" =

# ============================================
# Array Display
# ============================================

{
    "arr_name" local
    "size" local
    0 "i" local
    
    "[" .
    
print_loop:
    i size < "print_continue" if_jump
    "print_done" jump
    
print_continue:
    i arr_name array_get .
    
    i inc size < "need_comma" if_jump
    "no_comma" jump
    
need_comma:
    ", " .
    
no_comma:
    i inc "i" local
    "print_loop" jump
    
print_done:
    "]" print
} "array_print" =

# ============================================
# Array Aggregation
# ============================================

{
    "arr_name" local
    "size" local
    0 "total" local
    0 "i" local
    
sum_loop:
    i size < "sum_continue" if_jump
    "sum_done" jump
    
sum_continue:
    total i arr_name array_get + "total" local
    i inc "i" local
    "sum_loop" jump
    
sum_done:
    total
} "array_sum" =

{
    "arr_name" local
    "size" local
    0 arr_name array_get "min_val" local
    1 "i" local
    
min_loop:
    i size < "min_continue" if_jump
    "min_done" jump
    
min_continue:
    i arr_name array_get min_val min "min_val" local
    i inc "i" local
    "min_loop" jump
    
min_done:
    min_val
} "array_min" =

{
    "arr_name" local
    "size" local
    0 arr_name array_get "max_val" local
    1 "i" local
    
max_loop:
    i size < "max_continue" if_jump
    "max_done" jump
    
max_continue:
    i arr_name array_get max_val max "max_val" local
    i inc "i" local
    "max_loop" jump
    
max_done:
    max_val
} "array_max" =

{
    "arr_name" local
    "size" local
    size arr_name array_sum size /
} "array_average" =

# ============================================
# Array Manipulation
# ============================================

{
    "arr_name" local
    "size" local
    "val" local
    0 "i" local
    
fill_loop:
    i size < "fill_continue" if_jump
    "fill_done" jump
    
fill_continue:
    val i arr_name array_set
    i inc "i" local
    "fill_loop" jump
    
fill_done:
} "array_fill" =

{
    "dest_name" local
    "src_name" local
    "size" local
    0 "i" local
    
copy_loop:
    i size < "copy_continue" if_jump
    "copy_done" jump
    
copy_continue:
    i src_name array_get i dest_name array_set
    i inc "i" local
    "copy_loop" jump
    
copy_done:
} "array_copy" =

{
    "arr_name" local
    "size" local
    0 "left" local
    size dec "right" local
    
reverse_loop:
    left right < "reverse_continue" if_jump
    "reverse_done" jump
    
reverse_continue:
    left arr_name array_get "temp" local
    right arr_name array_get left arr_name array_set
    temp right arr_name array_set
    
    left inc "left" local
    right dec "right" local
    "reverse_loop" jump
    
reverse_done:
} "array_reverse" =

# ============================================
# Array Search
# ============================================

{
    "arr_name" local
    "size" local
    "val" local
    0 "i" local
    
find_loop:
    i size < "find_continue" if_jump
    "find_not_found" jump
    
find_continue:
    i arr_name array_get val ==
    "find_found" if_jump
    
    i inc "i" local
    "find_loop" jump
    
find_found:
    i
    "find_done" jump
    
find_not_found:
    -1
    
find_done:
} "array_find" =

{
    "arr_name" local
    "size" local
    "val" local
    
    val size arr_name array_find -1 >
} "array_contains" =

# ============================================
# Array Transformation
# ============================================

{
    "arr_name" local
    "size" local
    0 "i" local
    
map_loop:
    i size < "map_continue" if_jump
    "map_done" jump
    
map_continue:
    i arr_name array_get double i arr_name array_set
    i inc "i" local
    "map_loop" jump
    
map_done:
} "array_map_double" =

{
    "arr_name" local
    "size" local
    0 "i" local
    
sq_loop:
    i size < "sq_continue" if_jump
    "sq_done" jump
    
sq_continue:
    i arr_name array_get square i arr_name array_set
    i inc "i" local
    "sq_loop" jump
    
sq_done:
} "array_map_square" =

{
    "arr_name" local
    "size" local
    0 "read" local
    0 "write" local
    
filter_loop:
    read size < "filter_continue" if_jump
    "filter_done" jump
    
filter_continue:
    read arr_name array_get "val" local
    
    val 0 < "filter_skip" if_jump
    
    val write arr_name array_set
    write inc "write" local
    
filter_skip:
    read inc "read" local
    "filter_loop" jump
    
filter_done:
    write
} "array_filter_positive" =
