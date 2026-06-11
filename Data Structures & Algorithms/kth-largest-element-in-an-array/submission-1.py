class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if k > 0:
                heapq.heappush(heap, num)
                k -= 1
            else:
                heapq.heappushpop(heap, num)
        return heapq.heappop(heap)