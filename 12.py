class Solution:
    def intToRoman(self, num: int) -> str:
        roman = []
        high = num//1000
        for j in range(high):
            roman.append('M')
        num = num-high*1000
        high = num//100
        if high < 4:
            for j in range(high):
                roman.append('C')
        elif high == 4:
            roman.append('CD')
        elif high < 9:
            roman.append('D')
            for j in range(high-5):
                roman.append('C')
        else:
            roman.append('CM')
        num = num-high*100
        high = num//10
        if high < 4:
            for j in range(high):
                roman.append('X')
        elif high == 4:
            roman.append('XL')
        elif high < 9:
            roman.append('L')
            for j in range(high-5):
                roman.append('X')
        else:
            roman.append('XC')
        num = num-high*10
        high = num
        if high < 4:
            for j in range(high):
                roman.append('I')
        elif high == 4:
            roman.append('IV')
        elif high < 9:
            roman.append('V')
            for j in range(high-5):
                roman.append('I')
        else:
            roman.append('IX')
        return ''.join(roman)
