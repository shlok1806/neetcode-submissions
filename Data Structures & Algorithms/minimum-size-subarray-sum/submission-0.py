class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        

        R, L = 0, 0
        curr = 0
        res = float("inf")
        for R in range(len(nums)):
            curr += nums[R]
            
            while curr >= target:
                curr -= nums[L]
                res = min(res, R - L + 1)
                L += 1
        
        return 0 if res == float("inf") else res
