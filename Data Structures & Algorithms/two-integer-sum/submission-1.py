class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prvmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prvmap:
                return [prvmap[diff], i]
            prvmap[n] = i