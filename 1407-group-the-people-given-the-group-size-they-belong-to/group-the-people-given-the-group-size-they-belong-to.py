class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        szToGroup = defaultdict(list)
        
        for i, size in enumerate(groupSizes):
            szToGroup[size].append(i)
            
            if len(szToGroup[size]) == size:
                ans.append(szToGroup[size])
                szToGroup[size] = []
        
        return ans