import heapq
import math
import operator


class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, num * -1)

        if len(self.min_heap) > 0 and self.max_heap[0] * -1 > self.min_heap[0]:
            num = heapq.heappop(self.max_heap) * -1
            heapq.heappush(self.min_heap, num)

        while len(self.max_heap) - len(self.min_heap) > 1:
            num = heapq.heappop(self.max_heap) * -1
            heapq.heappush(self.min_heap, num)

        while len(self.min_heap) - len(self.max_heap) > 1:
            num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, num * -1)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return ((self.max_heap[0] * -1) + self.min_heap[0])/2
        elif len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0] * -1
        else:
            return self.min_heap[0]
