# LeetCode 155: Min Stack

# Implement the following operations in stack with O(1) time complexity

# push(elm), pop(), top(), getmin()

class MinStack():

    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []

    def push(self, elm):
        self.stack.append(elm)

        if not self.min_stack or elm < self.min_stack[-1]:
            self.min_stack.append(elm)
        
        return f"{elm} pushed in stack"
    
    def pop(self):
        val = self.stack[-1]
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

        return f"{val} is popped from stack"

    def top(self):
        return self.stack[-1]
    
    def get_min(self):
        return self.min_stack[-1]
    
    def view(self):
        return self.stack
    
obj = MinStack()
print(obj.push(1))
print(obj.push(2))
print(obj.top())
print(obj.push(0))
print(obj.view())
print(obj.get_min())
print(obj.pop())
print(obj.view())
print(obj.get_min())