
def threeSum(nums):
    target = 0 
    seen = set()

    nums_sorted = sorted(nums)
    
    final_array = []
    for i ,int in enumerate(nums_sorted):
        second_check = set() #in the for loop so it gets reset everytime. The only numbers that should be competely removed are the numbers added to seen
        if int in seen:
            continue #ignore the number it has already been used to check combinations 

        elif int not in seen:
            seen.add(int) #add to set the unique value that will be used to check sum combinations

            left = i + 1 #plus one becuase i is the current value we are checking  
            right = len(nums_sorted) -1 #last index 
           
            while left < right   : #This makes sure that the right pointer never crosses the left one and vise versa 

                #same number check 
                if nums_sorted[left] in second_check: #if left points to a already checked value, skip that value
                    left += 1 
                    continue

                if nums_sorted[right] in second_check: #if left points to a already checked value, skip that value
                    right -= 1 
                    continue

                #threeSum check 
                if nums_sorted[left] + nums_sorted[right] + int == 0 : # if they add up to target of 0 
                    final_array.append([int, nums_sorted[left], nums_sorted[right]]) #add it to answer 
                    right -= 1 #move both pointers
                    left +=1  #because 
                
                elif (nums_sorted[left] + nums_sorted[right] + int) > 0 :
                    right -= 1 # move the right pointer left as we are looking for a smaller number and the array is sorted
                    second_check.add(nums_sorted[right])
                
                else :
                    left +=1 #move left pointer one to the right as we need a bigger number
                    second_check.add(nums_sorted[left])
    
    
    return final_array

#test checks 
print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0]))