class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_string = s[0]
        for i in range(len(s)):
            rest_len = len(s)-i+1
            if len(max_string) > rest_len:
                return max_string            
            for j in range(len(s)-1,i,-1):
                flag = 1
                if s[i] == s[j]:
                    head = i
                    tail = j
                    while tail > head:
                        head += 1
                        tail -= 1
                        if s[head] != s[tail]:
                            flag = 0
                            break
                    if flag == 1:
                        if len(s[i:j+1])>len(max_string):
                            max_string = s[i:j+1]
        return max_string
