class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        l, r = 1, high
        res = r

        while l <= r:
            m = (l + r) // 2
            hours = 0
            for p in piles:
                time = math.ceil(p / m)
                hours += time
            if hours <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res