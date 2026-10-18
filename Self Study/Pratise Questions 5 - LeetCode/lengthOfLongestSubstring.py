

def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        substring = ""
        maxSubstring = 0 
    
        
        for chara in s :  # for each characters in s
            
            if chara in substring: # if character already exists in substring
                substring = substring[substring.index(chara)+1::] 

            
            substring = substring + chara #if no duplicate, 
            maxSubstring = max(maxSubstring, len(substring))
                
        
        return maxSubstring


print(lengthOfLongestSubstring("pwwkew"))
#print(lengthOfLongestSubstring("abcabcbb"))
#print(lengthOfLongestSubstring("bbbbb"))