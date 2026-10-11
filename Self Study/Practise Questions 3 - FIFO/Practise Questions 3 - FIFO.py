#Q1. What does FIFO mean, and how does it differ from LIFO? Give a real-world example of each.
# Fifo means first in first out. It simply means that the first objects added to the must be the first removed. 
# LIFO or last in first out means that the object that is added to the queue last will be the first removed. 
#FIFO in real life would be a normal queue to access a cashier. LIFO could be a stack of plates, the last plate put on top is the first to be used.

#Q2. Why is this a poor queue for large data? What’s the time complexity of pop(0) on a list, and what would you use instead?
#queue = []
#queue.append("a")
#queue.append("b")
#first = queue.pop(0) 

#A: The reason why this is not idea for large datasets is because Python dynamically allocates memory. So when you remove the first item from a list, python need to shift all 
#other values by one position to the left. Since there are n-1 items shifting left the time complexity is O(n). Rather than use a list its best to use 
#collections.deque as its popleft() is 0(1)


# Q3) What does this code print.
# from collections import deque
# q = deque([1, 2, 3]) 
# print(q) 

#A: it prints deque([1,2,3]). The trick to this question is that when you print out the whole queue made with collections.deque(), it also prints the wrapper to ensure 
# that is is differentiated from a list. (in other words it prints the dequeu object rather than the "queue" of values)

#Programming section.

#Q4) Build a Queue class with enqueue, dequeue, peek, is_empty, and size. Raise an error when dequeuing from an empty queue.

from collections import deque

class Queue :
   
    def __init__(self):
        self.items = deque()

    def enqueue(self, item) :
        self.items.append(item)
        

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

#Q5) Queue using two stacks (LIFO). Implement a FIFO queue using only two lists, where you may only use append() and pop() (no pop(0)).

class twoStackQueue() :

    def __init__(self):
        self.inbound = []
        self.outbound = []
    def queue(self,value): 
        self.inbound.append(value) # just add the values to inbound

    def dequeue(self):
        if self.outbound == [] : #need to check if outbound is empty otherwise adding to it will screw up the FIFO order
            while self.inbound != [] :  # pour inbound into outbound: this reverses the order, so the oldest item ends up on top
                self.outbound.append(self.inbound.pop()) 
        if self.outbound == [] :
            raise IndexError("dequeue from empty queue") 

        return self.outbound.pop()  # pop the last item from the outbound list as it's the first item queued


#Q6) round robin scheduler. works like a CPU 
def roundRobinScheduler(tasks):
    totalCompute = sum(tasks.values())  #total time (in compute) needed 
    taskList = deque()
    finished = []
    for key in tasks :
        taskList.append(key) 
    while totalCompute != 0 :
        totalCompute = totalCompute - 1 #decrement total compute time by 1 
        tasks[taskList[0]] = tasks[taskList[0]] -1 # decrement value of the first item in the tasklist 
        
        if tasks[taskList[0]] == 0 :#check if finished
            print(f"task {taskList[0]} is done ")
            finished.append(taskList.popleft())
        else :
            taskList.append(taskList.popleft()) # add first task to back of task list.

    return finished
        


    


    




#TESTS

#Q4   
#q = Queue()
#print(q.is_empty())    # True
#print(q.size())        # 0

#q.enqueue("a")
#q.enqueue("b")
#q.enqueue("c")
#print(q.size())        # 3
#print(q.is_empty())    # False

#print(q.peek())        # a
#print(q.size())        # 3   (peek didn't remove anything)

#print(q.dequeue())     # a
#print(q.dequeue())     # b
#print(q.size())        # 1
#print(q.peek())        # c

#q.enqueue("d")
#print(q.dequeue())     # c
#print(q.dequeue())     # d
#print(q.is_empty())    # True

#Q5   
#q = twoStackQueue()
#q.queue(1)
#q.queue(2)
#q.queue(3)
#print(q.inbound, q.outbound)   # [1, 2, 3] []

#print(q.dequeue())             # 1
#print(q.inbound, q.outbound)   # [] [3, 2]    (poured and reversed, 1 removed)

#q.queue(4)
#print(q.inbound, q.outbound)   # [4] [3, 2]   (4 waits in inbound)

#print(q.dequeue())             # 2            (no refill, outbound wasn't empty)
#print(q.dequeue())             # 3
#print(q.dequeue())             # 4            (outbound empty, so 4 is poured over)
#print(q.inbound, q.outbound)   # [] []

# Empty queue should raise your error
#try:
 #   q.dequeue()
#except IndexError as e:
#    print("error:", e)         # error: dequeue from empty queue

# Reuse after emptying, mixing queue and dequeue
#q.queue("a")
#q.queue("b")
#print(q.dequeue())             # a
#q.queue("c")
#print(q.dequeue())             # b
#print(q.dequeue())      


#Q6
#print(roundRobinScheduler({"A": 3, "B": 1, "C": 2}))          # ['B', 'C', 'A']   (the question's example)
#print(roundRobinScheduler({"A": 2}))                          # ['A']             (single task)
#print(roundRobinScheduler({"A": 1, "B": 1, "C": 1}))          # ['A', 'B', 'C']   (all finish on first turn)
#print(roundRobinScheduler({"A": 2, "B": 2}))                  # ['A', 'B']        (tie: original order wins)
#print(roundRobinScheduler({"A": 1, "B": 3, "C": 2}))          # ['A', 'C', 'B']
#print(roundRobinScheduler({"X": 4, "Y": 1, "Z": 3, "W": 2}))  # ['Y', 'W', 'Z', 'X']
#print(roundRobinScheduler({}))                                # []                (no tasks)