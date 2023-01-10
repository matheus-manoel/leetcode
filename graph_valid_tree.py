class Solution:
    def validTree(self, n, edges):
        if n == 1 and not edges:
            return True

        def build_graph():
            graph = {node: set() for node in range(n)}

            for i, j in edges:
                graph[i].add(j)
                graph[j].add(i)

            return graph

        def remove_edges_in_path(graph, node, visiteds):
            visiteds.add(node)

            for neigh in graph[node].copy():
                if neigh not in visiteds:
                    graph[node].remove(neigh)
                    graph[neigh].remove(node)
                    remove_edges_in_path(graph, neigh, visiteds)

        graph = build_graph()

        visiteds = set()
        remove_edges_in_path(graph, 0, visiteds)

        for edg in graph.values():
            if edg:
                return False

        if len(visiteds) != len(graph):
            return False

        return True
