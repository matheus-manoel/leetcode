import heapq


class Solution:
    def minMeetingRooms(self, intervals):
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        heap = [sorted_intervals[0][1]]
        max_n_of_rooms = 1

        for i in range(1, len(sorted_intervals)):
            interval = sorted_intervals[i]
            start, end = interval[0], interval[1]

            while len(heap) and start >= heap[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, end)

            max_n_of_rooms = max(max_n_of_rooms, len(heap))

        return max_n_of_rooms
