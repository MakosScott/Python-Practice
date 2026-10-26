
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        def get_length(head): #basic get lenght, just iterates until the next node is NONE and counts it up
            count = 0
            current = head
            while current is not None:
                count += 1
                current = current.next
            return count

        
        dummy = ListNode() #dummy node to store pointer to head 
        dummy.next = head 
       
        target = (get_length(head) - n)     #returns index of number to remove 
        
        current = dummy #current = dummy so we can work on the linked list wihout touching dummy (which will be used to return the head)

        for _ in range(target):         # target steps lands on index target - 1
            current = current.next      # since we start at dummy node which is technically index -1 (dummy -> head -> rest of list) we do not need target-1 

        current.next = current.next.next 
        
        return dummy.next
        



removeNthFromEnd([1,2,3,4,5], 2)