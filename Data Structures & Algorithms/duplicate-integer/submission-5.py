class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        out = set()

        for num in nums : 
            if num in out : 
                return True
            out.add(num)
        
        return False