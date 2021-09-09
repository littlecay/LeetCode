class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        li = [0 for i in range(0,m)]
        for i in range(len(arr)-m):
            flag = 1
            li = arr[i:i+m]
            for j in range(k):
                print(li,arr[i + j*m : (i+m) + j*m])
                if li != arr[i + j*m : (i+m) + j*m]:
                    flag = 0
                    break
            if flag == 1:
                return True
        if flag == 0:
            return False
