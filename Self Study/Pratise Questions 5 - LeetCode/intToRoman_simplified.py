def intToRoman_Simplified(num):
    RomanList = [["I",1],["IV",4],["V",5],["IX",9],["X",10],["XL",40],["L", 50],["XC",90],["C",100],["CD",400],["D",500],["CM",900],["M",1000]]
    final_string= ""
    for roman_symb, val in reversed(RomanList):
        if num // val :
            temp = num // val 
            final_string = final_string + (roman_symb*temp)
            num = num % val
            
    return final_string

print(intToRoman_Simplified(1500)) #MD
print(intToRoman_Simplified(3749)) #MMMDCCXLIX
print(intToRoman_Simplified(58)) #LVIII

