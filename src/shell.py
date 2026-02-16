from src.parser import execute
from src.lexer import tokenize
from src.ops.include_ops import reset_includes

print("Basalt version 1.1.0 (2026-02-07)")
print("Basalt is free software and comes with ABSOLUTELY NO WARRANTY.")
print("You are welcome to redistribute it under certain conditions")
print("of the MIT License. ")
print("")
print("Basalt is a minimalist stack-based language project")
print("")
print("Type 'exit' to quit Basalt.")

stack = [] 
    
while True:
    try:
        user_input = input("basalt >> ") 
            
        if user_input.lower() == "exit":
            break
        
        # Reset includes for each REPL command to allow re-including
        reset_includes()
                
        execute(tokenize(user_input), stack)
            
        print(f"Stack: {stack}")
            
    except Exception as e:
        print(f"Error: {e}")
