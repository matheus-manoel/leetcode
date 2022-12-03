class Solution:
    def merge(self, intervals):
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        merged_intervals = [sorted_intervals[0]]

        for i in range(1, len(sorted_intervals)):
            if merged_intervals[-1][1] >= sorted_intervals[i][0]:
                merged_intervals[-1][1] = max(
                        sorted_intervals[i][1],
                        merged_intervals[-1][1]
                        )
            else:
                merged_intervals.append(sorted_intervals[i])

        return merged_intervals
