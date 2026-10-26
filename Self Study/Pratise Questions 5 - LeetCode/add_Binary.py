
def add_Binary(a,b):
    carry = 0 
    holding_list = []
    
    for i in range(max(len(a),len(b)) -1,-1,-1) :
        
        tempsum = int(a[i]) + int(b[i]) + carry 
        carry = 0 
        if tempsum >= 2 : 
            tempsum -= 2 
            carry = 1
            holding_list.append(str(tempsum))
        else:
            holding_list.append(str(tempsum))
    
    if carry:                    # carry left over after the last digit
        holding_list.append("1")  

    return "".join(reversed(holding_list))
