class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
    
        non_overlapping = 0
        last_end = float('-inf')
    
        for start, end in intervals:
            if start >= last_end:
                last_end = end
                non_overlapping += 1
            
        return len(intervals) - non_overlapping
