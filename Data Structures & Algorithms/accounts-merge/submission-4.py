class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailId = {} # email to id 
        emails = [] # set of all emails 
        emailIDtoAcc = {} # email id to acc id 

        m = 0
        for accId, a in enumerate(accounts):
            for i in range(1, len(a)):
                email = a[i]
                if email in emailId:
                    continue
                emailId[email] = m
                emails.append(email)
                emailIDtoAcc[m] = accId
                m += 1
        

        adj = [[] for _ in range(m)]

        for a in accounts:
            for i in range(2, len(a)):
                idx1 = emailId[a[i]]
                idx2 = emailId[a[i - 1]]
                adj[idx1].append(idx2)
                adj[idx2].append(idx1)

        
        emailgroup = defaultdict(list) # index of accounts to list of emails 
        visited = [False] * m

        def dfs(node, accId):
            visited[node] = True
            emailgroup[accId].append(emails[node])
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei, accId)
        
        for i in range(m):
            if not visited[i]:
                dfs(i, emailIDtoAcc[i])
            
        res = []

        for accId in emailgroup:
            name = accounts[accId][0]
            res.append([name] + sorted(emailgroup[accId]))
        
        return res
        