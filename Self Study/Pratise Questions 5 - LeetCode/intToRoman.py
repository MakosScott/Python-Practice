def intToRoman(num):
        """
        :type num: int
        :rtype: str
        """
        
        romanInt = ""
        counter = len(str(num))
        strRep = str(num)
        while num != 0 : 
                strRep = str(num) 
                if strRep[0] != "4" and strRep[0] != "9"  : 
                    if num // 1000 :
                        temp = num // 1000
                        num = num - temp*1000
                        romanInt = "M"*temp 
                    elif num // 500 :
                        temp = num // 500
                        num = num - temp*500
                        romanInt =  romanInt + "D"*temp 
                    elif num // 100 :
                        temp = num // 100
                        num = num - temp*100
                        romanInt = romanInt + "C"*temp    
                    elif num // 50 :
                        temp = num // 50
                        num = num - temp*50
                        romanInt = romanInt + "L"*temp 
                    elif num // 10 :
                        temp = num // 10
                        num = num - temp*10
                        romanInt = romanInt + "X"*temp  
                    elif num // 5 :
                        temp = num // 5
                        num = num - temp*5
                        romanInt = romanInt + "V"*temp 
                    else : 
                        temp = num // 1
                        num = num - temp*1
                        romanInt = romanInt + "I"*temp 
                        
                elif strRep[0] == "4" or strRep[0] == "9"  :
                    if num // 900 :
                        num = num - 900
                        romanInt = romanInt + "CM"
                    elif num // 400 :
                        num = num - 400
                        romanInt = romanInt + "CD"   
                    elif num // 90 :
                        num = num - 90
                        romanInt = romanInt + "XC" 
                    elif num // 40 :
                        num = num - 40
                        romanInt = romanInt + "XL"
                    elif num // 9 :
                        num = num - 9
                        romanInt = romanInt + "IX"
                    else :
                        num = num - 4
                        romanInt = romanInt + "IX"
                   
        return romanInt

print(intToRoman(1500)) #MD
print(intToRoman(3749)) #MMMDCCXLIX
print(intToRoman(58)) #LVIII
        
        
          
                    

                
                