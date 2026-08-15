class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        map_s = defaultdict(int)
        map_t = defaultdict(int)

        for c in s : 
            map_s[c] += 1 
        for c in t : 
            map_t[c] += 1

        return map_t == map_s
