class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n = len(s1)
        count1 = {}

        for c in s1:
            count1[c] = 1 + count1.get(c, 0)
        
        for i in range(len(s2)):
            curr = {}
            for j in range(i, len(s2)):        
                curr[s2[j]] = 1 + curr.get(s2[j], 0)

                if curr == count1: 
                    return True
            print(curr)
        
        return False