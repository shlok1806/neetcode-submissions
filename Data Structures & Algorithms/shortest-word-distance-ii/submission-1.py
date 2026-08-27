class WordDistance:

    def __init__(self, words: List[str]):
        self.locations = defaultdict(list)

        # Prepare a mapping from a word to all it's locations (indices).
        for i, w in enumerate(words):
            self.locations[w].append(i)


    def shortest(self, word1: str, word2: str) -> int:
        loc1 = self.locations[word1]
        loc2 = self.locations[word2]

        l1 = 0 
        l2 = 0 
        minDiff = float("inf")
        while l1 < len(loc1) and l2 < len(loc2):
            minDiff = min(minDiff, abs(loc1[l1] - loc2[l2]))

            if loc1[l1] < loc2[l2]:
                l1 += 1
            else:
                l2 += 1
            
        
        return minDiff