from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        my_counter = Counter(nums)

        for i in my_counter.most_common(k):
            ans.append(i[0])

        return ans