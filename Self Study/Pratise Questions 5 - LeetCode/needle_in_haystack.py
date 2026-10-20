
def needle_in_haystack(haystack,needle):
    if needle in haystack:
            return haystack.find(needle) # str.find(substring) returns the index at which the substring starts in str
    else :
        return -1
