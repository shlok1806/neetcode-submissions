class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        countS1 = {}

        n = len(s1)

        for c in s1:
            countS1[c] = 1 + countS1.get(c, 0)
        
        for i in range(len(s2) - n + 1):
            curr = {}
            for j in range(i, i + n):

                curr[s2[j]] = 1 + curr.get(s2[j], 0)
                
            if curr == countS1:
                return True
        
        return False