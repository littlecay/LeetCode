class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        while s[i] == ' ':
            i = i - 1
        if i == -1:
            return 0
        j = i
        while s[j] != ' ' and j >= 0:
            j = j - 1
        return i-j
