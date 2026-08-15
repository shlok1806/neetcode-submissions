class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sumMap = defaultdict(int)
        
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if sumMap[tmp]:
                return [sumMap[target - numbers[i]], i + 1 ] 
            sumMap[numbers[i]] = i + 1
        return []