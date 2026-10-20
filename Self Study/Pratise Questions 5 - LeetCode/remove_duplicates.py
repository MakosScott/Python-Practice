#Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. 
# Then return the number of elements in nums which are not equal to val.
#Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
#Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
#The remaining elements of nums are not important as well as the size of nums.
#Return k.



def remove_duplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        write_pointer = 1 #this is the pointer that will write the values into the array 
    
        for i in range(1, len(nums)) : #skip first value since it will always be the smallest. (list is sorted) 
            if nums[i] != nums[i-1]:
                nums[write_pointer]= nums[i]
                write_pointer += 1 #increment pointer by 1  so that it points to the index where the next value will be stored
        
        print(nums)              
        return write_pointer 



print(remove_duplicates([1,1,2]))
print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))