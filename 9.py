class Solution:
    def isPalindrome(self, x: int) -> bool:
        upper_lim = 1
        lower_lim = 1
        if x < 0:
            return False
        if x < 10:
            return True
        while x>=upper_lim:
            print(1)
            upper_lim = upper_lim * 10
        while upper_lim//10>=lower_lim:
            print(x % (lower_lim*10)//lower_lim, x//(upper_lim//10)%(10))
            if x % (lower_lim*10)//lower_lim == x//(upper_lim//10)%(10):
                print(3)
                lower_lim = lower_lim * 10
                upper_lim = upper_lim // 10
            else:
                return False
        return True
