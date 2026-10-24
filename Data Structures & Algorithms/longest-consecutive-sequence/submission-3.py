class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxVal = 0
        numsSet = set(nums)

        for num in nums:
            count = 0
            if (num - 1) not in numsSet:
                while (num + count) in numsSet:
                    count += 1
                maxVal = max(maxVal, count)
        return maxVal