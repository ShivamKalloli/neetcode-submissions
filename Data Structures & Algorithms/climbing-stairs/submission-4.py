from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dfs(i):
            if i >= n:
                return n == i
            return dfs(i + 1) + dfs(i + 2)
        return dfs(0)