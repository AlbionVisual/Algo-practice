from collections import deque

class Stack():
    """Simple stack to work with deque through 5th lab"""
    def __init__(self, data = []):
        self.items = deque(data)

    def __len__(self):
        return len(self.items)
    
    def is_empty(self):
        return bool(len(self))

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if len(self) <= 0: print("stack is empty")
        return self.items.pop()
    
    def peek(self):
        if len(self) <= 0: print("stack is empty")
        else: return self.items[-1]