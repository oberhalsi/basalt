from parser import execute
from lexer import tokenize
print("Basalt v1.0 Shell")
print("Type 'exit' to quit.")
    
stack = [] 
    
while True:
    try:
        user_input = input("basalt >> ") 
            
        if user_input.lower() == "exit":
            break
                
        execute(tokenize(user_input), stack)
            
        print(f"Stack: {stack}")
            
    except Exception as e:
        print(f"Error: {e}")