class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        out = defaultdict(int)

        for i in range(len(nums)) : 
            if target - nums[i] in out : 
                return [out[target - nums[i]], i ]
            out[nums[i]] = i 
        
        return [-1, -1]