# Advanced Array Tests

"array" include

"=== Test 1: Aggregation ===" print
5 "nums" array_new
10 0 "nums" array_set
50 1 "nums" array_set
30 2 "nums" array_set
20 3 "nums" array_set
40 4 "nums" array_set

5 "nums" array_print
"Sum: " . 5 "nums" array_sum print
"Min: " . 5 "nums" array_min print
"Max: " . 5 "nums" array_max print
"Avg: " . 5 "nums" array_average print

newline

"=== Test 2: Fill ===" print
99 5 "filled" array_fill
5 "filled" array_print

newline

"=== Test 3: Copy ===" print
5 "nums" "copy" array_copy
5 "copy" array_print

newline

"=== Test 4: Reverse ===" print
5 "nums" array_reverse
5 "nums" array_print

newline

"=== Test 5: Find ===" print
30 5 "nums" array_find print
999 5 "nums" array_find print

newline

"=== Test 6: Contains ===" print
30 5 "nums" array_contains print
999 5 "nums" array_contains print

newline

"=== Test 7: Map Double ===" print
5 "test" array_new
1 0 "test" array_set
2 1 "test" array_set
3 2 "test" array_set
4 3 "test" array_set
5 4 "test" array_set

5 "test" array_print
5 "test" array_map_double
5 "test" array_print

newline

"=== Test 8: Map Square ===" print
5 "sq" array_new
1 0 "sq" array_set
2 1 "sq" array_set
3 2 "sq" array_set
4 3 "sq" array_set
5 4 "sq" array_set

5 "sq" array_print
5 "sq" array_map_square
5 "sq" array_print

newline

"=== Test 9: Filter Positive ===" print
6 "mixed" array_new
-5 0 "mixed" array_set
10 1 "mixed" array_set
-3 2 "mixed" array_set
20 3 "mixed" array_set
-1 4 "mixed" array_set
15 5 "mixed" array_set

6 "mixed" array_print
6 "mixed" array_filter_positive "new_size" =
"New size: " . new_size print
new_size "mixed" array_print
