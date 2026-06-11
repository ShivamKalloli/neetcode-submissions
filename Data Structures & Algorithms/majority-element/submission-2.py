class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        greatest = None
        max_count = 0
        for k, v in count.items():
            if max_count < v:
                max_count = v
                greatest = k
        return greatest