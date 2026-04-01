class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #what about just using an array?
        #we have an array where each index is the number of ocrncs
        #and each value is the actual numbers that are there
        #we can count occurenes with a hashmap, and then add those
        #values to the array
        occurrences = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            occurrences[num] += 1

        for num in set(nums):
            freq[occurrences[num]].append(num)
        
        res = []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

            


        