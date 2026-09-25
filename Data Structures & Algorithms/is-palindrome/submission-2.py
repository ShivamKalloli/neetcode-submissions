class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

    # def alnum(self, c):
    #     return (ord('A') <= ord(c) <= ord('Z')
    #             ord('a') <= ord(c) <= ord('z')
    #             ord('0') <= ord(c) <= ord('9'))