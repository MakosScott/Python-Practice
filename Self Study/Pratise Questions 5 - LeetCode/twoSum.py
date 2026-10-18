

#Example 1:

#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#Example 2:

#Input: nums = [3,2,4], target = 6
#Output: [1,2]
#Example 3:

#Input: nums = [3,3], target = 6
#Output: [0,1]
 

#Constraints:

#2 <= nums.length <= 104
#-109 <= nums[i] <= 109
#-109 <= target <= 109
#Only one valid answer exists.
 

#Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


def twoSum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums) : #lets you loop through index and value 
        num2 = target - num #calculated for every number 

        if num2 in seen:  #if the target you need is in seen, return it's index (value of the key:value) and the current index 
            print(seen[num2],i) # just for testing
            return [seen[num2],i]

        seen[num] = i #otherwise add the current index and its value to the dict
    
    print([])# just for testing
    return[] #return nothing if no combination was made


twoSum([3,2,4], 6)
twoSum([3,3],6)
twoSum([3,2],6)