class Solution:
    def findMin(self, nums: List[int]) -> int:
        hi, lo = len(nums) -  1, 0


        while hi > lo:

            mid = (hi + lo) // 2

            if nums[mid] >= nums[hi]:
                lo = mid + 1
            else:
                hi = mid 

        return nums[lo]