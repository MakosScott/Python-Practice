#Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
#You must write an algorithm with O(log n) runtime complexity.

 
#Example 1:

    #Input: nums = [1,3,5,6], target = 5
    #Output: 2



def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) -1
        
        while left <= right :
            mid = left + (right-left) //2
            mid_val = nums[mid]
            if mid_val == target :
                return mid 
            elif mid_val > target : #go left 
                 right = mid -1
            elif mid_val < target : #go right 
                 left = mid +1 

        return left 
               

searchInsert([1,3,5,6],7)