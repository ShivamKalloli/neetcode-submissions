class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        longest = 0
        
        for num in nums:
            if (num - 1) not in setnums:
                curLen = 1

                while (num + curLen) in setnums:
                    curLen += 1
                
                longest = max(longest, curLen)
        return longest