# LeetCode 150: Evaluate Reverse Polish Notation

# You are given an array of string tokens that represents an arithematic expression in a reverse polish notation.
# Evaluate the expression, return a value that represents the value of the expression.

# token = ['1','2','+','4','*','5','-']
# output = 7

def evaluate_exp(a,b,opr):
    if opr == '+':
        return a + b
    elif opr == '-':
        return a - b
    elif opr == '*':
        return a * b
    elif opr == '/':
        return a/b
    else:
        return None

def rpn(token):
    
    stack = []
    n = len(token)
    
    for i in range(n):
        if token[i] in '+-*/':
            b = stack.pop()
            a = stack.pop()
            val = evaluate_exp(a,b,token[i])
            if val is not None:
                stack.append(val)
            else:
                return None
        else:
            stack.append(int(token[i]))
        
        print(stack)
    
    return stack[-1]

result = rpn(['1','2','+','4','*','5','-'])
print(result)