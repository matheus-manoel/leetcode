class Solution:
    def findRedundantConnection(self, edges):
        graph = {x: [] for x in range(1, len(edges) + 1)}
        visiting_snapshot = []

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def dfs(src, visiteds=None, visiting=None, previous=None):
            nonlocal visiting_snapshot

            if visiteds is None:
                visiteds = set()

            if visiting is None:
                visiting = set()

            if src in visiting:
                print(visiting)
                visiting_snapshot.append([previous, src])
                return

            if src in visiteds:
                return

            visiteds.add(src)
            visiting.add(src)

            for neigh in graph[src]:
                dfs(neigh, visiteds, visiting, src)

            visiting.remove(src)

        dfs(1)

        for edge in reversed(edges):
            for snapshot in visiting_snapshot:
                if edge[0] in snapshot and edge[1] in snapshot:
                    return edge

        return [-1, -1]
