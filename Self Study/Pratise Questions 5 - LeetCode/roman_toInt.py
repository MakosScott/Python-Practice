def roman_toInt(s) :
    """
    :type s: str
    :rtype: int
    """
    dict = {"I" : 1, "V" :5, "X": 10, "L":50, "C":100, "D":500, "M" :1000} #dict to store permanent value associated with each roman numeral
    sum = 0 
    i = 0 
    while i < len(s)-1 : #len -1 assures there is no need out of bound access
    
        if dict[s[i]] >= dict[s[i+1]]  :
            sum = sum + dict[s[i]]
            i = i+1
            
        elif dict[s[i]] < dict[s[i+1]] : # if the number in front is smaller, then there must be a substaction.
            sum = sum - dict[s[i]]
            i = i +1  # skip two numbers since both were accounted for 
    
    sum += dict[s[-1]]  #always add last character 
    return sum 
        
        
print(roman_toInt("III"))
print(roman_toInt("LVIII"))
print(roman_toInt("MCMXCIV"))