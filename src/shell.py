from src.parser import execute
from src.lexer import tokenize
from src.ops.include_ops import reset_includes

print("Basalt v1.0.1 Shell")
print("Type 'exit' to quit.")
    
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
