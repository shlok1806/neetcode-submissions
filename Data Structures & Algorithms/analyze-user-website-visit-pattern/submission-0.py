class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        arr = list(zip(timestamp, username, website))
        arr.sort()
        mp = defaultdict(list)
        for timestamp, name, site in arr: 
            mp[name].append(site)

        count = defaultdict(int)

        for user in mp: 
            patterns = set()

            cur = mp[user]
            for i in range(len(cur)):
                for j in range(i + 1, len(cur)):
                    for k in range(j + 1, len(cur)):
                        patterns.add((cur[i], cur[j], cur[k]))

            
            for p in patterns: 
                count[p] += 1
        
        maxCount = 0 

        res = tuple()


        for pattern in count: 
            if count[pattern] > maxCount or (count[pattern] == maxCount and pattern < res):
                maxCount = count[pattern]
                res = pattern

        return list(res)