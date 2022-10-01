from collections import deque


class Solution:
    def numBusesToDestination(self, routes, source, target):
        graph = {}
        added = set()

        for route in routes:
            for i in range(len(route)):
                for j in range(i+1, len(route)):
                    stop_1 = route[i]
                    stop_2 = route[j]
                    if (stop_1, stop_2) not in added:
                        if stop_1 in graph:
                            graph[stop_1].append(stop_2)
                        else:
                            graph[stop_1] = [stop_2]
                        if stop_2 in graph:
                            graph[stop_2].append(stop_1)
                        else:
                            graph[stop_2] = [stop_1]
                        added.add((stop_1, stop_2))
                        added.add((stop_2, stop_1))

        def get_min_distance_bfs():
            q = deque()
            discovered = set()
            distances = {node: None for node in graph}

            q.append(source)
            discovered.add(source)
            distances[source] = 0

            while q:
                work_node = q.popleft()

                for neigh in graph[work_node]:
                    if neigh not in discovered:
                        q.append(neigh)
                        discovered.add(neigh)
                        distances[neigh] = distances[work_node] + 1
            
            return distances

        distance_from_source = get_min_distance_bfs()

        return distance_from_source[target] if distance_from_source[target] is not None else -1
