class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        we need to return the top k element occurences in an array
        we can do this by having an array where the index is the number of times
        an element appears, and the value is the actual value
        we can initialize a hashmap where the key is the value, and value is number of times
        then, we need an array of arrays as a response
        this array will have all items that have occurence of 1 into freq[1]
        after this, we look through this array backwards, and put that into the response
        array

        '''
        counts = {}
        frequencies = [[] for i in range(len(nums) + 1)]
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        for num, cnt in counts.items():
            # at the frequency index, we need to append the number
            frequencies[cnt].append(num)
        
        '''
        now, we need to intitialize the response array
        and there, iterate through the array backwards, and append into the new array
        the top k numbers
        '''
        res = []
        for i in range(len(frequencies) - 1, 0, -1):
            for num in frequencies[i]:
                res.append(num)
                if len(res) == k:
                    return res