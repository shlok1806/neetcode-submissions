class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        r, l = 1,0
        currSum = 0 
        count = 0
        for r in range(len(arr)):
            currSum += arr[r]

            if r - l + 1 == k:
                if (currSum/k) >= threshold:
                    count += 1
                currSum -= arr[l]
                l += 1
                

        return count