class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[l]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = (l + r) // 2

            if nums[mid] >= nums[r]:
                l = mid + 1
                res = min(res, nums[mid])
            elif nums[mid] <= nums[l]:
                r = mid - 1
                res = min(res, nums[mid])


        return res