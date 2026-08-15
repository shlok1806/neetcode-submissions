class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        r, l = len(nums) - 1, 0
        nums.sort()
        for i in range(len(nums)):
            l = i + 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while r > l:
                if nums[i] + nums[r] + nums[l] > 0:
                    r -= 1

                elif nums[i] + nums[r] + nums[l] < 0:
                    l += 1

                elif nums[i] + nums[r] + nums[l] == 0:
                    out.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                
            r = len(nums)  - 1
        return out
                
