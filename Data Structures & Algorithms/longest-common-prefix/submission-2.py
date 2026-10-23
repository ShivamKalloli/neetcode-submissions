class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s1, s2 = min(strs), max(strs)

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return s1[:i]
        return s1