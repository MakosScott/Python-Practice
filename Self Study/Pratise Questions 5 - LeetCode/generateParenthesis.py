
def generateParenthesis(n) :
    """
    :type n: int
    :rtype: List[str]
    """
    result = []
    stack = []

    def backtrack(open, closed):
        if open == closed == n : #if open==closed==n then there is no more recursion to be had  
            result.append("".join(stack)) #add this option to result list 
            return 

        if open < n : #if open <n add an open parenthesis (
            stack.append("(")
            backtrack(open+1, closed) #run the method but with open+1 to open count 
            stack.pop() #pop it off so we can evaluate the other examples

        if closed < open :
            stack.append(")") #if closed < open  add an closed parenthesis )
            backtrack(open,closed +1)
            stack.pop()
    
    backtrack(0,0) #starts the recursive method. 
    return result    
    
    
    
    
    