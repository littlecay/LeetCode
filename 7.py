class Solution:
    def reverse(self, x: int) -> int:
        num = list(str(x))
        # i = len(num)-1
        new = []
        res = 0
        time = 1
        signal = 1
        if  num[0] ==  '-':
            signal = -1
            num.pop(0)
        # print(num)
        while num[0] == 0:
            num.pop(0)
        while len(num) > 0:
            new.append(num.pop(-1))
        # print(new)
        for i in range(len(new)-1, -1, -1):
            # print(i)
            res = int(new[i]) * time + res
            time = time * 10
        ret =  res * signal
        if ret < 0 and len(bin(ret).replace('0b',''))>32:
            return 0
        if ret > 0 and len(bin(ret).replace('0b',''))>31:
            return 0
        else:
             return ret
