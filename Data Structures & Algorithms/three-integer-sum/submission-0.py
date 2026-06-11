class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            l, r = i + 1 , len(nums) - 1
            if i > 0 and nums[i-1] == nums[i]:
                continue
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l +=1
                else:
                    res.append([nums[l], nums[r], nums[i]])
                    l +=1
                    r -=1
                    while l < r and nums[l] == nums[l-1]:
                        l +=1
                    while l < r and nums[r] == nums[r+1]:
                        r -=1
        return res