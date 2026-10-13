class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        arr = list(zip(timestamp, username, website))
        arr.sort()

        mp = defaultdict(list)
        for time, user, site in arr: 
            mp[user].append(site)

        
        count = defaultdict(int)
        for user in mp: 
            pattern = set()
            cur = mp[user]
            for i in range(len(cur)):
                for j in range(i + 1, len(cur)):
                    for k in range(j + 1, len(cur)):
                        pattern.add((cur[i], cur[j], cur[k]))

            for p in pattern:
                count[p] += 1
                 
        maxCount = 0
        res = tuple()
        for p in count: 
            if (count[p] > maxCount) or (count[p] == maxCount and p < res):
                maxCount = count[p]
                res = p

        return list(res)