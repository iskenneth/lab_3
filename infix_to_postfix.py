from lab_4 import LinkedList

def operands_position (op):
    if op ('+', '-'):
        return 1
    if op ('*','/'):
        return 2
    return 0

def infix_topostfix(expression):
    stack = LikedList()
    output = []

    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(': 
            stack.insert_at_end (char)
        elif char ')':
            while stack.head and stack.tail.data != '(':
                output.append(stack.remove_at_end())
            stack.remove_at_end()
        else:
            while stack.head and operands_position(stack.tail.data)>= operands_position(char):
                output.append(stack.remove_at_end())
            stack.insert_at_end(char) 
    while stack.head:
        output.append(stack.remove_at_end())
    return " ".join(output)              

            

    
    
    