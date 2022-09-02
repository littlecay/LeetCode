class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        ans = (r-l)//2
        while not (ans*ans<x and (ans+1)*(ans+1)>x):
            if ans*ans>x:
                r = ans
                ans = l + (r-l)//2
            elif (ans+1)*(ans+1)<x:
                l = ans
                ans = l + (r-l)//2
            if ans*ans == x:
                return ans
            if (ans+1)*(ans+1) == x:
                return ans+1
        return ans
