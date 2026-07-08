class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ok so the logic for this is that we can sort all the words in the list and then group them but this will take 
        # O(nlogn times m ) where n is the avg length of the word in the list and m is the size of the list/number of elems in the list 
        #  here sorting each elem takes nlogn time and we have to do that m times 


        # OPTIMAL APPROACH : 
        # so here the optimal approach is to use a hash table 
        # so we are going to use a count array of size 26 (for each alphabet) and for each word we will have an array where each position of the array will indicate the number of times we see that alphabet 
        # then we can group all the words in the list who have the same array 

        res = defaultdict(list) # we use lists for this case 

        for w in strs : 
            count = [0] * 26 

            for c in w : 

                count[ord(c) - ord("a")] += 1
            # we use a tuple because it is immutable and only immutable objects can be a key in python 
            res[tuple(count)].append(w) 

        return list(res.values())