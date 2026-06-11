class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        u, v = {}, {}
        for i in s:
            if i in u:
                u[i] += 1
            else:
                u[i] = 1
        for j in t:
            if j in v:
                v[j] += 1
            else:
                v[j] = 1
        return u == v