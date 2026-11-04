from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        buckets = [[] for _ in range(len(nums)+1)]

        for x, freq in count.items():
            buckets[freq].append(x)
        
        result = []

        for freq in range(len(nums), 0 , -1):
            for x in buckets[freq]:
                result.append(x)
                if len(result) == k:
                    return result