
#Given a string s consisting of words and spaces, return the length of the last word in the string.
#A word is a maximal substring consisting of non-space characters only.

#Example 1:
    #Input: s = "Hello World"
    #Output: 5


#Explanation: The last word is "World" with length 5.

def lengthOfLastWord(s):
        """
        :type s: str
        :rtype: int
        """
        words = s.strip().split() #remove all extra spaces and split up each word
        print(words) #just to visualize results 
        return len(words[-1]) #return lenght of last word


lengthOfLastWord("Hello World")
lengthOfLastWord("   fly me   to   the moon  ")
lengthOfLastWord("luffy is still joyboy")