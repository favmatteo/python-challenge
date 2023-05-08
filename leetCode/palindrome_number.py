class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
    
print(Solution().isPalindrome(121))