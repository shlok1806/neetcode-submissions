class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r, l = len(numbers) - 1, 0 

        while r > l: 
            if numbers[r] + numbers[l] == target:
                return [l + 1, r + 1]

            if numbers[r] + numbers[l] > target:
                r -= 1
            if numbers[r] + numbers[l] < target: 
                l += 1
        
        return []