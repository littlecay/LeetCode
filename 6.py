class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # residual = len(s) % numRows
        if numRows == 1:
            return s
        s1 = []
        row = 0
        point = 0
        i = numRows
        dist = 2 * i - 2
        while len(s1) < len(s):
            print(point,dist)
            s1.append(s[point])
            point = (point + dist)
            if dist != 2 * numRows -2:
                dist = 2 * numRows -2 - dist
            if point >= len(s):
                row = row + 1
                i = i - 1
                if i == 1:
                    i = numRows
                dist = 2 * i - 2
                point = row
        return ''.join(s1)
