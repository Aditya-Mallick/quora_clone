from collections import defaultdict, deque


class Solution:
    def findOrder(self, n: int, prereq):
        adj = defaultdict(set)
        for cou, pre in prereq:
            adj[cou].add(pre)

        visit = set()
        done = set()
        q = deque()
        ans = []

        for i in range(n):
            if i not in adj:
                done.add(i)
                ans.append(i)

        def dfs(i, cur):
            visit.add(i)
            for nei in adj[i]:
                if nei in visit:
                    return False, []
                if nei in done:
                    continue
                a, b = dfs(nei, cur)
                if not a:
                    return False, []
            visit.remove(i)
            cur.append(i)
            done.add(i)
            return True, cur

        for i in range(n):
            if i in done:
                continue
            a, b = dfs(i, [])
            if not a:
                return []
            for j in b:
                ans.append(j)
                done.add(j)

        return ans


obj = Solution()
print(obj.findOrder(2, [[0, 1]]))
