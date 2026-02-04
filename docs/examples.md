# Basalt Examples

Complete working programs and code snippets.

---

## Hello World

### Basic Hello World
```basalt
"Hello, World!" print
```

### Hello World with Variable
```basalt
"Hello, World!" "message" =
"message" call print
```

### Hello World Function
```basalt
{ "Hello, World!" print } "greet" =
"greet" call run
```

---

## Calculator Programs

### Simple Calculator
```basalt
"=== Calculator ===" print
newline

# Addition
5 10 + print

# Subtraction  
20 7 - print

# Multiplication
6 7 * print

# Division
100 5 / print
```

### Interactive Calculator
```basalt
"Enter first number: " . in
"Enter second number: " . in

"Sum: " . 2 pick 2 pick + print
"Difference: " . 2 pick 2 pick swap - print
"Product: " . 2 pick 2 pick * print
"Quotient: " . swap / print
```

---

## Working with Variables

### Store and Retrieve
```basalt
42 "answer" =
"The answer is: " . "answer" call print
```

### Multiple Variables
```basalt
100 "health" =
50 "mana" =
10 "level" =

"Health: " . "health" call print
"Mana: " . "mana" call print
"Level: " . "level" call print
```

### Update Variables
```basalt
0 "counter" =
"counter" call print    # 0

"counter" call 1 + "counter" =
"counter" call print    # 1

"counter" call 1 + "counter" =
"counter" call print    # 2
```

---

## Functions with Code Blocks

### Square Function
```basalt
{ dup * } "square" =

5 "square" call run print     # 25
10 "square" call run print    # 100
```

### Multiple Functions
```basalt
# Define functions
{ dup * } "square" =
{ dup dup * * } "cube" =
{ 2 * } "double" =

# Use them
5 "square" call run print    # 25
3 "cube" call run print      # 27
7 "double" call run print    # 14
```

### Function Composition
```basalt
{ dup * } "square" =
{ 2 * } "double" =

# Square then double
{ "square" call run "double" call run } "square_double" =

5 "square_double" call run print    # 50
```

---

## Conditional Programs

### Simple If-Else
```basalt
10 "x" =

"x" call 0 > "positive" if_jump

"Number is not positive" print
"done" jump

positive:
    "Number is positive" print

done:
```

### Grade Calculator
```basalt
85 "score" =

"score" call 90 >= "grade_a" if_jump
"score" call 80 >= "grade_b" if_jump
"score" call 70 >= "grade_c" if_jump
"score" call 60 >= "grade_d" if_jump

"Grade: F" print
"done" jump

grade_a:
    "Grade: A" print
    "done" jump

grade_b:
    "Grade: B" print
    "done" jump

grade_c:
    "Grade: C" print
    "done" jump

grade_d:
    "Grade: D" print

done:
```

### Even or Odd
```basalt
{ 2 % 0 == } "is_even" =

7 "number" =

"number" call "is_even" call run "even" if_jump

"number" call . " is odd" print
"done" jump

even:
    "number" call . " is even" print

done:
```

---

## Loops

### Count to 10
```basalt
0 "i" =

loop:
    "i" call 10 < "continue" if_jump
    "done" jump

continue:
    "i" call print
    "i" call 1 + "i" =
    "loop" jump

done:
```

### Sum from 1 to N
```basalt
10 "n" =
0 "sum" =
1 "i" =

loop:
    "i" call "n" call > "done" if_jump
    
    "sum" call "i" call + "sum" =
    "i" call 1 + "i" =
    "loop" jump

done:
    "Sum: " . "sum" call print
```

### Factorial
```basalt
5 "n" =
1 "result" =
"n" call "i" =

loop:
    "i" call 0 == "done" if_jump
    
    "result" call "i" call * "result" =
    "i" call 1 - "i" =
    "loop" jump

done:
    "n" call . "! = " . "result" call print
```

### Multiplication Table
```basalt
5 "n" =
1 "i" =

loop:
    "i" call 10 > "done" if_jump
    
    "n" call . " x " . "i" call . " = " . "n" call "i" call * print
    "i" call 1 + "i" =
    "loop" jump

done:
```

---

## Interactive Programs

### Guessing Game
```basalt
42 "secret" =
0 "guesses" =

loop:
    "Guess the number: " . in
    "guesses" call 1 + "guesses" =
    
    dup "secret" call == "correct" if_jump
    dup "secret" call > "too_high" if_jump
    
    drop
    "Too low! Try again." print
    "loop" jump

too_high:
    drop
    "Too high! Try again." print
    "loop" jump

correct:
    drop
    "Correct! You guessed it in " . "guesses" call . " tries!" print
```

### Simple Menu
```basalt
menu:
    newline
    "=== Menu ===" print
    "1. Say Hello" print
    "2. Print Numbers" print
    "3. Exit" print
    "Choice: " . in
    
    dup 1 == "option1" if_jump
    dup 2 == "option2" if_jump
    dup 3 == "exit" if_jump
    
    drop
    "Invalid choice!" print
    "menu" jump

option1:
    drop
    "Hello, User!" print
    "menu" jump

option2:
    drop
    1 print
    2 print
    3 print
    "menu" jump

exit:
    drop
    "Goodbye!" print
```

### Calculator with Menu
```basalt
menu:
    newline
    "=== Calculator ===" print
    "1. Add" print
    "2. Subtract" print
    "3. Multiply" print
    "4. Divide" print
    "5. Exit" print
    "Choice: " . in
    
    dup 5 == "exit" if_jump
    
    "Enter first number: " . in
    "Enter second number: " . in
    
    3 pick 1 == "add" if_jump
    3 pick 2 == "subtract" if_jump
    3 pick 3 == "multiply" if_jump
    3 pick 4 == "divide" if_jump

add:
    + "Result: " . print
    drop
    "menu" jump

subtract:
    swap - "Result: " . print
    drop
    "menu" jump

multiply:
    * "Result: " . print
    drop
    "menu" jump

divide:
    swap / "Result: " . print
    drop
    "menu" jump

exit:
    drop
    "Goodbye!" print
```

---

## String Programs

### Name Greeter
```basalt
"What's your name? " . in
"Hello, " swap str+ "!" str+ print
```

### Build Sentence
```basalt
"Alice" "name" =
"developer" "job" =

"name" call " is a " str+ "job" call str+ print
```

### Title Generator
```basalt
"The Great " "title_prefix" =

"Enter your name: " . in
"title_prefix" call swap str+ print
```

---

## Math Programs

### Area of Circle
```basalt
# Using π ≈ 3.14
{ dup * 314 * 100 / } "circle_area" =

10 "circle_area" call run print    # ≈ 314
```

### Temperature Converter
```basalt
# Celsius to Fahrenheit
{ 9 * 5 / 32 + } "c_to_f" =

# Fahrenheit to Celsius
{ 32 - 5 * 9 / } "f_to_c" =

0 "c_to_f" call run print      # 32
32 "f_to_c" call run print     # 0
100 "c_to_f" call run print    # 212
```

### Fibonacci Numbers
```basalt
# Print first 10 Fibonacci numbers
0 "a" =
1 "b" =
0 "i" =

loop:
    "i" call 10 >= "done" if_jump
    
    "a" call print
    
    "a" call "b" call +
    "a" call "b" =
    "a" =
    
    "i" call 1 + "i" =
    "loop" jump

done:
```

### Prime Number Check
```basalt
17 "n" =
2 "i" =
1 "is_prime" =

check:
    "i" call "n" call >= "done" if_jump
    
    "n" call "i" call % 0 == "not_prime" if_jump
    
    "i" call 1 + "i" =
    "check" jump

not_prime:
    0 "is_prime" =

done:
    "is_prime" call "prime" if_jump
    "n" call . " is not prime" print
    "end" jump

prime:
    "n" call . " is prime" print

end:
```

---

## Using Libraries

### With Standard Library
```basalt
"std.b" include

# Use built-in functions
5 "square" call run print
3 "cube" call run print
10 "double" call run print
7 "is_even" call run print
```

### Building Your Own Library

**mylib.b:**
```basalt
# My Math Library

{ dup * } "square" =
{ dup dup * * } "cube" =
{ dup 0 < { 0 swap - } { } if_jump } "abs" =
```

**main.b:**
```basalt
"mylib.b" include

-5 "abs" call run print     # 5
4 "square" call run print   # 16
2 "cube" call run print     # 8
```

---

## Real-World Programs

### BMI Calculator
```basalt
"Enter weight (kg): " . in "weight" =
"Enter height (m): " . in "height" =

# BMI = weight / height²
"weight" call
"height" call dup *
/
"bmi" =

"Your BMI: " . "bmi" call print

"bmi" call 18.5 < "underweight" if_jump
"bmi" call 25 < "normal" if_jump
"bmi" call 30 < "overweight" if_jump

"Category: Obese" print
"done" jump

underweight:
    "Category: Underweight" print
    "done" jump

normal:
    "Category: Normal" print
    "done" jump

overweight:
    "Category: Overweight" print

done:
```

### Simple To-Do List
```basalt
0 "count" =

menu:
    newline
    "=== To-Do List ===" print
    "Items: " . "count" call print
    "1. Add item" print
    "2. Exit" print
    "Choice: " . in
    
    dup 1 == "add" if_jump
    dup 2 == "exit" if_jump
    
    drop
    "Invalid!" print
    "menu" jump

add:
    drop
    "Enter item: " . in
    " added" str+ print
    "count" call 1 + "count" =
    "menu" jump

exit:
    drop
    "Goodbye!" print
```

### Number Statistics
```basalt
"How many numbers? " . in "n" =
0 "sum" =
0 "i" =

input_loop:
    "i" call "n" call >= "calculate" if_jump
    
    "Enter number: " . in
    "sum" call swap + "sum" =
    "i" call 1 + "i" =
    "input_loop" jump

calculate:
    "Sum: " . "sum" call print
    "Average: " . "sum" call "n" call / print
```

---

## Tips for Writing Programs

1. **Start simple** - Get basic version working first
2. **Test frequently** - Run code after each addition
3. **Use variables** - Store intermediate results
4. **Comment code** - Explain what you're doing
5. **Build functions** - Reuse common operations
6. **Handle errors** - Check for invalid input
7. **Format output** - Make it readable for users

---

## Practice Exercises

Try building these yourself:

1. **Rock Paper Scissors** - Play against the computer
2. **Count Vowels** - Count vowels in a string (needs string ops)
3. **Decimal to Binary** - Convert number to binary
4. **Palindrome Checker** - Check if number is palindrome
5. **Grade Book** - Store and average multiple grades
6. **Simple Bank** - Deposit, withdraw, check balance
7. **Countdown Timer** - Count down from N to 0
8. **Math Quiz** - Random math questions (needs random)

---

Happy coding! Build something awesome! 🪨