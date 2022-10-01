import heapq


class Solution:
    def networkDelayTime(self, times, n, k):
        graph = {x: [] for x in range(1, n+1)}

        for time in times:
            src = time[0]
            dst = time[1]
            weight = time[2]
            graph[src].append((dst, weight))

        def dijkstra(src):
            unvisiteds = set(range(1, n+1))
            distances = {x: float('inf') for x in range(1, n+1)}

            distances[src] = 0
            heap = [(0, src)]

            while heap:
                _, visiting = heapq.heappop(heap)

                if visiting in unvisiteds:
                    unvisiteds.remove(visiting)

                    for neigh, weight in graph[visiting]:
                        if (neigh in unvisiteds 
                                and distances[visiting] + weight < distances[neigh]):
                            new_dist = distances[visiting] + weight
                            distances[neigh] = new_dist
                            heapq.heappush(heap, (new_dist, neigh))

            return distances, unvisiteds

        distances_from_k, unvisiteds = dijkstra(k)

        return -1 if len(unvisiteds) > 0 else max(distances_from_k.values())
