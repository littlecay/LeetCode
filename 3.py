class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        l = 0
        r = 0
        s1 = list(s)
        cur = 0
        ll = 1
        max = 0
        while r < len(s1)-1:
            r += 1
            ll += 1
            while s1[r] in s1[l:r]:
                l += 1
                ll -= 1
            if ll > max:
                # print(s1[l:r],s1[l],s1[r])
                max = ll
        return max
