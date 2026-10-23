class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res = maxVal = 0
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            if count[num] > maxVal:
                res = num
                maxVal = count[num]
        return res