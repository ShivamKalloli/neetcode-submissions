class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {']' : '[', '}' : '{', ')' : '('}

        for bracket in s:
            if bracket in matching:
                if stack and stack[-1] == matching[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return not stack