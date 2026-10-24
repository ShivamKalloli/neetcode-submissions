class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        res = set()
        minVal = (len(nums) // 3)

        for num in nums:
            count[num] += 1
            if count[num] > minVal:
                res.add(num)
        return list(res)