class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs[0]) == 0: return ""
        
        first_letter = strs[0][0]
        for word in strs:
            if not word.startswith(first_letter):
                return ""
        letter_in_common = strs[0][0]
        for letter in strs[0][1:]:
            letter_in_common += letter
            for word in strs:
                if not word.startswith(letter_in_common):
                    return letter_in_common[:-1]

        
        return letter_in_common

print(Solution().longestCommonPrefix(["flower","flow","flight"]))