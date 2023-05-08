class Solution:
    def romanToInt(self, s: str) -> int:
        conversion = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        res = 0
        exclude = False
        for i in range(len(s)):
            if exclude:
                exclude = False
                continue
            if i+1 >= len(s):
                res += conversion[s[i]]

            elif s[i] == 'I' and s[i + 1] in ('V', 'X'):
                res += conversion[s[i + 1]] - 1
                exclude = True

            elif s[i] == 'X' and s[i + 1] in ('L', 'C'):
                res += conversion[s[i + 1]] - 10
                exclude = True

            elif s[i] == 'C' and s[i + 1] in ('D', 'M'):
                res += conversion[s[i + 1]] - 100
                exclude = True

            else:
                res += conversion[s[i]]
        return res
    
s = Solution()
print(s.romanToInt('MCMXCIV'))

1000
