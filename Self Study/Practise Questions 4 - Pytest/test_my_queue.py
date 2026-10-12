# testing my_queue.py
from my_queue import Queue

#enqueue() function must: 1.add an item into the queue. 2. the item must be added to the end 3. size of queue must go up by 1.

def test_size_increase_after_enqueue():
    #initialize queue to test 
    q = Queue()
    q.enqueue("Brian")

    assert q.size() == 1  #does this new queue increase in size (to 1) after enqueue() is called

def test_peek_returns_first_item(): 
    q = Queue()
    q.enqueue("Brian")
    q.enqueue("Scott")

    assert q.peek()== "Brian"

def test_dequeue_removes_first_item():
    q = Queue()
    q.enqueue("Brian")
    q.enqueue("Scott")
    q.enqueue("Rowan")

   
    assert q.dequeue == "Brian"
    assert q.size == 2

# Testing is_empty after initializing the Queue, after adding items and after removing all items
def test_new_queue_is_empty():
    q = Queue()
    assert q.is_empty() is True


def test_not_empty_after_enqueue():
    q = Queue()
    q.enqueue("a")
    assert q.is_empty() is False


def test_empty_again_after_dequeuing_everything():
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    q.dequeue()
    assert q.is_empty() is False    # "b" still in queue"
    q.dequeue()
    assert q.is_empty() is True


#TESTING 
#If there is not AssertionError post running the functions, the tests have passed.

#test_size_increase_after_enqueue()
test_peek_returns_first_item()
