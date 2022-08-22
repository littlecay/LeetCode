class Solution:
    def myAtoi(self, s: str) -> int:
        num = list(s)
        signal = 1
        new = []
        time = 1
        res = 0
        # print(num)
        if '0' not in num and '1' not in num and '2' not in num and '3' not in num and '4' not in num and '5' not in num and '6' not in num and '7' not in num and '8' not in num and '9' not in num:
            return 0
        while num[0] == ' ':
            num.pop(0)
        if num[0] == '+':
            num.pop(0)
        elif num[0] == '-':
            signal = -1
            num.pop(0)
        while len(num)>=1 and num[0] in '0123456789' :
            new.append(num.pop(0))
        print(new)
        for i in range(len(new)-1,-1,-1):
            res = int(new[i]) * time + res
            time = time * 10
        ret =  res * signal
        if ret < -2**31:
            return -2**31
        if ret > 2**31-1:
            return 2**31-1
        else:
             return ret
