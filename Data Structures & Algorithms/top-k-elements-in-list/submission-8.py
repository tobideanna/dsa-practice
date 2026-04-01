class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1

        for i in range(k):
            max_key = max(hashmap, key=hashmap.get)
            result.append(max_key)
            del hashmap[max_key]
            
        return result
        