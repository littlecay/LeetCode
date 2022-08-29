class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            # print(stack)
            if i == '(' or i == '[' or i =='{':
                stack.append(i)
            else:
                if stack == []:
                    return False
                if (i == ')' and stack[-1] == '(') or (i == ']' and stack[-1] == '[') or (i == '}' and stack[-1] == '{'):
                    stack.pop(-1)
                else:
                    return False
        if stack == []:
            return True
        else:
            return False
