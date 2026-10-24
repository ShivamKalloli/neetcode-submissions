class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxVal = 0
        numsSet = set(nums)

        for num in numsSet:
            if (num - 1) not in numsSet:
                count = 1
                while (num + count) in numsSet:
                    count += 1
                maxVal = max(maxVal, count)
        return maxVal