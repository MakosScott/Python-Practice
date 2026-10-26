def lettercombinations(digits):
    if not digits :
        return []
    
    phone = {"2":"abc","3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8" : "tuv", "9":"wxyz" }
    
    result = []

    def backtrack(i,path):
        if i == len(digits): # if we on the last number,
            result.append("".join(path)) # turn the list of strings into a string and add it to result (as path holds )
            return 
        for letter in phone[digits[i]]: # for each letter corresponding to the number digits[i]
            path.append(letter) # append the letter to the end of the current list of letters
            backtrack(i+1, path) #recursion call which goes to next number in digts and passes the currently built string list 
            path.pop() #remove the letter so when we .append(letter) the next letter associated to the digit it does not contain the previous one 

    backtrack(0,[]) #start of recursion (we are on the first number i= 0 and have an empty list which holds our current path)
    return result