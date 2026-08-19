class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        
        count = 0
        for i in range(0, len(arr) - k + 1):
            subArrSum = 0
            for j in range(i, i + k):
                subArrSum += arr[j]
            if (subArrSum) / k >= threshold:
                count += 1
        
        return count