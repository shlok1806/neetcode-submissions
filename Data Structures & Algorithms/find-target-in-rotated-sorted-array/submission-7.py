class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        
        
        while l < r:
            mid = (l + r) // 2
            print(l,mid,r)

            if nums[mid] == target:
                return mid
            
            if nums[l] < nums[mid]:
                if nums[mid] < target or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid
            else:
                if nums[mid] > target or target > nums[r]:
                    r = mid
                else:
                    l = mid + 1


        return -1