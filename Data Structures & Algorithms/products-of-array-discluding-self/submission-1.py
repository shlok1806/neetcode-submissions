class Solution:
    def productExceptSelf(self, nums):
        total = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                total *= num
            else:   
                zero_count += 1
        res = [0] * len(nums)
        if zero_count >= 2:
            return res
        if zero_count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = total   # rest stay 0 from initialization
            return res
        for i in range(len(nums)):
            if nums[i] != 0:
                res[i] = total // nums[i]   # integer division (but still not allowed by follow‑up)
            else:
                res[i] = total
        return res 
