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
        popped = self.items.pop()
        self.sift_down(0)
        return popped

    def get_data(self):
        return self.items
    
    def sift_up(self, i):
        while i >= 1 and self.items[i] < self.items[(i-1)//2]:
            self.items[i], self.items[(i-1)//2] = self.items[(i-1)//2], self.items[i]
            i = (i-1)//2

    def sift_down(self, i):
        while (2*i + 1 < len(self) and self.items[i] > self.items[2*i + 1]) or (2*i + 2 < len(self) and self.items[i] > self.items[2*i + 2]):
            if (2*i + 2 < len(self) and self.items[2*i + 2] > self.items[2*i + 1]):
                self.items[i], self.items[2*i + 1] = self.items[2*i + 1], self.items[i]
                i = 2*i + 1
            elif (2*i + 2 < len(self)):
                self.items[i], self.items[2*i + 2] = self.items[2*i + 2], self.items[i]
                i = 2*i + 2
            else:
                self.items[i], self.items[2*i + 1] = self.items[2*i + 1], self.items[i]
                i = 2*i + 1



# from random import randrange
# if __name__ == '__main__':

#     h1 = MinHeap()
#     for _ in range(10):
#         h1.push(randrange(1, 100))
    
#     while not h1.is_empty():
#         print(h1.pop(), end = ' ')
    
#     print(h1.peek())