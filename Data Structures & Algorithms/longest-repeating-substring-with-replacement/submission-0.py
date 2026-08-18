class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # YYYY  k = 2

        # HFHHHFFH k = 2 freq[F] = 3 freq[H] = 5 

        freq = {}
        res = 0
        maxFreq = 0
        l = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
   
            maxFreq = max(maxFreq, freq[s[r]])
            while (r - l + 1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
                
            res = max(r - l + 1, res)

        return res

