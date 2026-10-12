#Testing code from Practice Questions 3 - FIFO


from collections import deque 
class Queue :
   
    def __init__(self):
        self.items = deque()

    def enqueue(self, item) :
        self.items.append(item) #this function must: 1.add an item into the queue. 2. the item must be added to the end 3. size of queue must go up by 1.
        

    def dequeue(self) :
        if self.is_empty():
            raise IndexError("The queue is empty. There is nothing to dequeue")    
        else :
           return self.items.popleft() 
    
    def peek(self) :
        if self.is_empty():
            raise IndexError("The queue is empty. There is nothing to peek at")    
        return(self.items[0]) 

    def is_empty(self): 
        if len(self.items) == 0 :
            return True
        else: 
            return False

    def size(self): 
            return len(self.items)