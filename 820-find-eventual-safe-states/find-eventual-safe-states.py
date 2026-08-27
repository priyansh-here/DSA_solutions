class Solution:
    def eventualSafeNodes(self, graph):
        state = [0] * len(graph)

        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True

            state[node] = 1

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            state[node] = 2
            return True

        return [i for i in range(len(graph)) if dfs(i)]