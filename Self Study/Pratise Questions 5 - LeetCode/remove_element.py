#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k.


def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    write_pointer = 0 #since first value could be val, we need to possibly replace it as well. 
    for n in nums : #check every number in nums. 
        if n != val : #if its not val, write it to front of array 
            nums[write_pointer] = n #assign it to write_pointer position
            write_pointer += 1 #increment point

    return (write_pointer) #since index[0] must be accounted for 


#Note for review : If you are going to use n in nums, you must make sure you remember that n refers to the value not an index. 
# so nums[n] would mean the value at the index of the value n.