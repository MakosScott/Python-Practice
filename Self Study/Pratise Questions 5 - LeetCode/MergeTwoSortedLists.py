
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    dummy = ListNode()
    final_list = dummy
    while list1 is not None and list2 is not None:  #if any of the list are not empty 
        
        if list1.val <= list2.val : # if the value of list 1 is smaller than list 2 current val, add it to final list and move along the linked list 1
            
            final_list.next = list1
            final_list = final_list.next 
            list1 = list1.next #move l1 pointer to next node as previous node was added 
        
        
        elif list2.val < list1.val : # if the value of list 2 is smaller than list 1 current val, add it to final list
            final_list.next = list2
            final_list = final_list.next 
            list2 = list2.next #move l2 pointer to next node as previous node was added 

    if list1 is not None : #add rest of list 1 if its not empty 
        final_list.next = list1

    elif list2 is not None : #add rest of list 2 if its not empty 
            final_list.next = list2

    return dummy.next
        
