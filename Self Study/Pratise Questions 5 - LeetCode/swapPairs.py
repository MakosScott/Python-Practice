class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




def swapPairs(head):

    dummy = ListNode()
    dummy.next = head 
    prev = dummy  

    while head :
        if head.next == None:
            return dummy.next

        elif head.next :
            temp = head.next  #hold the node head.next (2)
            head.next = head.next.next #assign (1)->(3)
            temp.next = head #(temp or 2)->(1)->(3)
            prev.next = temp 
            
            prev = head #set dummy.next (what we return to new front temp)
            head = head.next # move to node 3 

    return dummy.next
        
         