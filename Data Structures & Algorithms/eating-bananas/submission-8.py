class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r, l = max(piles), 1 
        res = 0 

        while r >= l: 
            k = (r + l) // 2
            time = 0
            for p in piles: 
                time += math.ceil(p / k)
            
            if time <= h: 
                res = k 
                r = k - 1
            else : 
                l = k + 1
        
        return res