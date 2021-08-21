from typing import List
class Solution:
    def shortestCompletingWord(licensePlate: str, words: List[str]) -> str:
        backup = []
        word = 'aaaaaaaaaaaaaaa'
        standard = [0 for i in range(0,26)]
        for i in licensePlate.lower():
            if ord(i) in range(ord('a'),ord('z')):
                standard[ord(i)-ord('a')] += 1
        for i in words:
            alphabeta = [0 for j in range(0,26)]
            flag = 0
            for k in i:
                alphabeta[ord(k)-ord('a')] += 1
            for check in range(0,26):
                if alphabeta[check]<standard[check]:
                    flag = 1
                    break
            if flag == 0:
                backup.append(i)
        for new in backup:
            if len(new) < len(word):
                word = new
        return word

sess = Solution.shortestCompletingWord("1s3 456",["looks","pest","stew","show"])
print(sess)