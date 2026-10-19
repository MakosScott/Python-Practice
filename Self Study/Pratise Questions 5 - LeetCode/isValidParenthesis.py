from collections import deque

def isValidParenthesis(s): 
    queue = []
    
    for chara in s: 
        if chara == "[" or chara == "{" or chara == "(" :
            queue.append(chara)

        elif chara == "]" :
            if queue[-1] == "[" :
                queue.pop()
            else :
                return False
        
        elif chara == "}" :
            if queue[-1] == "{" :
                queue.pop()
            else :
                return False
                    
        elif chara == ")" :
            if queue[-1] == "(" :
                queue.pop()
            else :
                return False
                    
    return True
        
print(isValidParenthesis("()"))     #True
print(isValidParenthesis("()[]{}")) #True
print(isValidParenthesis("(]"))     #False
print(isValidParenthesis("([])"))   #True
print(isValidParenthesis("([)]"))   #False