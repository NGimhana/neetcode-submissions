from collections import defaultdict
from heapq import heapify, heappop, heappush
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = defaultdict(int)

        for num in nums:
            frequencyMap[num]+=1  ## {2: 1, 3:2, 4:1} --> [2,3,3,3,4]

        heap =  []

        for num, count in frequencyMap.items():
            heapq.heappush(heap, (count,num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res



        
        