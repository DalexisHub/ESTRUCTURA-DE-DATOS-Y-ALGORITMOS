def infix_to_postfix(tokens):
    """Convert infix expression to postfix notation"""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    postfix = []
    
    for token in tokens:
        # Operand case
        if token not in ['+', '-', '*', '/', '(', ')']:
            postfix.append(token)
        # Opening parenthesis
        elif token == '(':
            stack.append(token)
        # Closing parenthesis
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
        # Operator case
        else:
            while (stack and stack[-1] != '(' and 
                   stack[-1] in precedence and 
                   precedence.get(stack[-1], 0) >= precedence.get(token, 0)):
                postfix.append(stack.pop())
            stack.append(token)
    
    # Empty remaining operators from stack
    while stack:
        postfix.append(stack.pop())
    
    return postfix


# Test cases
# Test 1: Simple addition
print("Test 1:", infix_to_postfix(['2', '+', '3']) == ['2', '3', '+'])

# Test 2: Operator precedence
print("Test 2:", infix_to_postfix(['2', '+', '3', '*', '4']) == ['2', '3', '4', '*', '+'])

# Test 3: Parentheses override precedence
print("Test 3:", infix_to_postfix(['(', '2', '+', '3', ')', '*', '4']) == ['2', '3', '+', '4', '*'])