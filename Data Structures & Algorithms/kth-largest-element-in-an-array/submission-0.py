class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        while k > 0:
            x = heapq.heappop(nums)
            x = -x
            k -= 1
        return x