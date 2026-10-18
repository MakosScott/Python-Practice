# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def addTwoNumbers(l1, l2):
        
        #:type l1: Optional[ListNode]
        #:type l2: Optional[ListNode]
        #:rtype: Optional[ListNode]
       
    #generate linked list for non-leetcode testing
    l1 = build(l1)
    l2 = build(l2)    
    
    dummy = ListNode()  #first node is a dummy node. when returning answer, you will 
    result = dummy
    carry = 0 
    sum = 0  
    while l1 or l2 or carry :
        sum =  carry #add values 
        if l1 != None :
            sum = sum + l1.val
            l1 = l1.next  # move pointer on non-finished list 
        if l2 != None :
            sum = sum + l2.val
            l2= l2.next 

        carry = 0 #reset carry for current loop as it was accounted for  
        
        
        if sum >= 10 : # if sum is higher than 10 add 1 to carry, reduce sum by 10
            sum = sum-10 
            carry = 1 

        result.next = ListNode(sum)  #adding node with Sum to the return linked list 
        result = result.next # move pointer to newly added node 


    print(dummy.next)
    return(dummy.next) # you return based on dummy node as dummy.next is the start of result[ListNode]

def build(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next




print(addTwoNumbers([2,4,3], [5,6,4]))