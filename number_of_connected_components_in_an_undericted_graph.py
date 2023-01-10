class Solution:
    def countComponents(self, n, edges):
        def build_graph():
            graph = {node: [] for node in range(n)}
            
            for dst, src in edges:
                graph[src].append(dst)
                graph[dst].append(src)

            return graph

        def dfs(graph, src, visiteds):
            visiteds.add(src)

            for neigh in graph[src]:
                if neigh not in visiteds:
                    dfs(graph, neigh, visiteds)

        counter = 0
        visiteds = set()
        graph = build_graph()
        for i in range(n):
            if i not in visiteds:
                dfs(graph, i, visiteds)
                counter += 1

        return counter
