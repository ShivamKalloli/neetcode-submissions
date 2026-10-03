class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {')':'(', ']':'[','}':'{'}

        for char in s:
            if char in bracket:
                if stack and stack[-1] == bracket[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack