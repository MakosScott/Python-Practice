
#i need to check if there is a palindrom within the string and then return it 

def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)] #populate a n * n matrix with all values set to false
        ans = [0, 0]

        for i in range(n): # we know all i = j (single letter) are palindromes so set all those values to True
            dp[i][i] = True

        for i in range(n - 1): # lenght 2 strings if the character is beside itself, then you have a 2 lenght palindrome
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        for diff in range(2, n): # for all string that are larger than 2 (diff is the distance from the start to the end of the substring)
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]: # if the outskirts are equal and the middle section (in the matrix is true) you know its palindroms
                    dp[i][j] = True
                    ans = [i, j]

        i, j = ans
        return s[i : j + 1]
        


