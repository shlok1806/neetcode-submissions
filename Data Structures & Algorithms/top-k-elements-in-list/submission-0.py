class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we could start with a hashmap and analyse the performance ot see if we can do any better 
        # first approach : i am thinking that if we use a hashmap right now then we will only have to do one pass through the array 
        # maybe we could improve the spatial complexity later 


        res = {}
        freq = [[] for i in range(len(nums) +1)]
        for num in nums : 
            res[num] = 1 + res.get(num, 0)

        for n,c in res.items() :
            freq[c].append(n)
        ans = []
        for i in range(len(freq) - 1, 0 , -1) :
            for num in freq[i] :
                ans.append(num)
                if len(ans) == k:
                    return ans

        return ans
