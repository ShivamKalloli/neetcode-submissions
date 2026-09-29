class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if not (n - 1) in numSet:
                curLen = 1

                while (n + curLen) in numSet:
                    curLen += 1

                longest = max(curLen, longest)
        return longest