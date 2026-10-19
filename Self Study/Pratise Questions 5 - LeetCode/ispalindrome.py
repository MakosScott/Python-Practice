
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    string_number = str(x)

    if string_number[::] == string_number[::-1] :
        return True
    else:
        return False

print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
print(isPalindrome(1010101))