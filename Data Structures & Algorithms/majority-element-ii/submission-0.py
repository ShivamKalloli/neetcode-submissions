class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        res = set()
        minVal = (len(nums) // 3)

        for num in nums:
            count[num] = 1 + count.get(num, 0)
            if count[num] > minVal:
                res.add(num)
        return list(res)