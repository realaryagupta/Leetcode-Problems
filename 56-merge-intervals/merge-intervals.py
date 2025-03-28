class Solution:
    def merge(self, intervals):
        # Step 1: Handle the case of empty input
        if not intervals:
            return []
    
        # Step 2: Sort the intervals based on the starting value
        intervals.sort(key=lambda x: x[0])
    
        merged = []
    
        for interval in intervals:
            # If merged list is empty or there is no overlap with the last interval, add it
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Merge the intervals by updating the end time
                merged[-1][1] = max(merged[-1][1], interval[1])
    
        return merged
