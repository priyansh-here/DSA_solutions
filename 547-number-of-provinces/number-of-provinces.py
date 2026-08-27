class Solution:
    def findCircleNum(self, isConnected):
        visited = set()
        ans = 0

        def dfs(i):
            visited.add(i)
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and j not in visited:
                    dfs(j)

        for i in range(len(isConnected)):
            if i not in visited:
                ans += 1
                dfs(i)

        return ans 