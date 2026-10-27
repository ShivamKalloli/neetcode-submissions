class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = float('inf')
        sum = 0
        
        for r in range(len(nums)):
            sum += nums[r]
            if sum >= target:
                res = min(res, r - l + 1)
                while sum >= target and l <= r:
                    res = min(res, r - l + 1)
                    sum -= nums[l]
                    l += 1
        return res if res != float('inf') else 0