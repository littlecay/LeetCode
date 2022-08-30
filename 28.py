class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)>len(haystack):
            return -1
        if needle == '':
            return 0
        for i in range(len(haystack)):
            flag = 0        
            if haystack[i] == needle[0]:
                for j in range(len(needle)):
                    # print(i,j)
                    if i+j >=len(haystack):
                        return -1
                    if needle[j] != haystack[i+j]:
                        print(flag)
                        flag = 1
                        break
                if flag == 0:
                    return i
        return -1        
