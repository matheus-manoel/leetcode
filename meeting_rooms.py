class Solution:
    def canAttendMeetings(self, intervals):
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i - 1][1] > sorted_intervals[i][0]:
                return False

        return True
