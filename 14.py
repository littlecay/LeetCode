class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        num = len(strs)
        min_l = 200
        com__pre = []
        if len(strs) == 1:
            return strs[0]
        for k in strs:
            if k == '':
                return ''
            if len(k)<min_l:
                min_l = len(k)   
        for j in range(min_l):
            for i in range(num):
                if strs[i][j] != strs[0][j]:
                    return ''.join(com__pre)
            com__pre.append(strs[0][j])
        return ''.join(com__pre)
