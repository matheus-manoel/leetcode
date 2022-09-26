class Graph:
    def __init__(self):
        self.edges = {}

    def build_graph(self, prerequisites):
        for prerequisite in prerequisites:
            src, dst = prerequisite[0], prerequisite[1]

            if src in self.edges:
                self.edges[src].append(dst)
            else:
                self.edges[src] = [dst]

            if dst not in self.edges:
                self.edges[dst] = []

    '''
    def discover_has_cycle(self, node, visited=None, still_visiting=None):
        if not visited:
            visited = set()

        if not still_visiting:
            still_visiting = set()

        visited.add(node)
        still_visiting.add(node)

        for neighbor in self.edges[node]:
            if neighbor in still_visiting:
                self.has_cycle = True
            if neighbor not in visited:
                self.discover_has_cycle(neighbor, visited, still_visiting)

        still_visiting.remove(node)
    '''


class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = Graph()
        graph.build_graph(prerequisites)
        print(graph.edges)

        def has_cycle_dfs(node, visited=None, still_visiting=None):
            if visited is None:
                visited = set()

            if still_visiting is None:
                still_visiting = set()

            if node in still_visiting:
                return True

            if node in visited:
                return False

            visited.add(node)
            still_visiting.add(node)

            for neighbor in graph.edges[node]:
                if has_cycle_dfs(neighbor, visited, still_visiting):
                    return True

            still_visiting.remove(node)

            return False

        for course in range(numCourses):
            if course in graph.edges:
                if has_cycle_dfs(course):
                    return False

        return True
