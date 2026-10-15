class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapS1 = defaultdict(int)

        for c in s1:
            mapS1[c] += 1
        
        for i in range(len(s2) - len(s1) + 1): 
            curr = defaultdict(int)
            for j in range(i, i + len(s1)):
                curr[s2[j]] += 1
                if mapS1.get(s2[j], 0) < curr[s2[j]]:
                    break
            if curr == mapS1:
                return True

        
        return False