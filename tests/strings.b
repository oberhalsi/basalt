# String Operations Test

# Test str+
"Hello" " " str+ "World" str+ print

# Test split_chars
"Hi" split_chars
print  # Count: 2
print  # H
print  # i

newline

# Test int_to_str
42 int_to_str print
-10 int_to_str print
0 int_to_str print

# Test str_to_int
"123" str_to_int print
"-50" str_to_int print
"0" str_to_int print

# Test conversion roundtrip
999 int_to_str str_to_int print

# Build dynamic variable name
"var_" 5 int_to_str str+ print
