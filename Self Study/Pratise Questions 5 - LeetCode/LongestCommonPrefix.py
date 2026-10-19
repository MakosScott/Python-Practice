def LongestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    prefix = ""
    len_smallest_str=  min(len(s) for s in strs)
    x = 0 
    letters = strs[0]
    for i in range(len_smallest_str):
        for word in strs[1:] :  #strs[1:] so that it does not compare the first word with itself n-1 intead of n
            if word[i] != letters[i]:
                return prefix
            else :
                continue #if the letters match add that letter to the end of 
        prefix = prefix + letters[i]    
    return prefix        
        
print(LongestCommonPrefix(["flower","flow","flight"]))    
print(LongestCommonPrefix(["dog","racecar","car"]))  
   