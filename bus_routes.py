from collections import deque


class Solution:
    def numBusesToDestination(self, routes, source, target):
        stop_to_routes = {}
        for i, route in enumerate(routes):
            for stop in route:
                if stop not in stop_to_routes:
                    stop_to_routes[stop] = set()
                stop_to_routes[stop].add(i)

        def get_min_distance_bfs():
            discovered_stops = set()
            discovered_routes = set()
            q = deque()
            distances = {x: -1 for x in stop_to_routes.keys()}

            discovered_stops.add(source)
            q.append(source)
            distances[source] = 0

            while q:
                work_node = q.popleft()

                for route_i in stop_to_routes[work_node]:
                    if route_i not in discovered_routes:
                        for neigh in routes[route_i]:
                            if neigh not in discovered_stops:
                                q.append(neigh)
                                discovered_stops.add(neigh)
                                distances[neigh] = distances[work_node] + 1
                        discovered_routes.add(route_i)

            return distances

        res = get_min_distance_bfs()
        return res[target] if target in res else -1

print(Solution().numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12))



'''
class Solution2:
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
'''
