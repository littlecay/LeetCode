class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for i in s:
            if ord(i) in range(ord('a'),ord('z')+1) or (ord(i) in range(ord('0'),ord('9')+1)):
                res.append(i)
            elif ord(i) in range(ord('A'),ord('Z')+1):
                res.append(chr(ord(i)-ord('A')+ord('a')))
        print(res)
        i = 0
        j = len(res)-1
        while i<j:
            print(i,j)
            if res[i] != res[j]:
                return False
            i += 1
            j -= 1
        return True
