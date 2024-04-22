class MinHeap:
    
    def __init__(self):
        self.items = []
    
    def __len__(self):
        return len(self.items)

    def is_empty(self):
        return len(self) <= 0

    def peek(self):
        if self.is_empty(): return "heap is empty"
        else: return self.items[0]
    
    def push(self, item):
        self.items += [item]
        self.sift_up(len(self) - 1)

    def pop(self):
        self.items[0], self.items[-1] = self.items[-1], self.items[0]
        self.items.pop()
        self.sift_down(0)

    def get_data(self):
        return self.items
    
    def sift_up(self, i):
        ...

    
    def sift_down(self, i):
        while self.items[i] < self.items[(i-1)//2]:
            self.items[i], self.items[(i-1)//2] = self.items[(i-1)//2], self.items[i]
            i = (i-1)//2



# from time import time
# from random import random
# if __name__ == '__main__':

#     start = time()
#     s1 = Stack()
#     for _ in range(100000):
#         s1.enqueue(random())
    
#     while not s1.is_empty():
#         s1.dequeue()
    
#     print(time() - start, s1.peek())