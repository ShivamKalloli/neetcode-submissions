class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        greatest = None
        max_count = 0
        for k, v in count.items():
            if max_count < count[k]:
                max_count = count[k]
                greatest = k
        return greatest