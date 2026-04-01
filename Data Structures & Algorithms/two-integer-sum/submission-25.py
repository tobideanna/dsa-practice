class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #so two sum. we need to return the pairs such that the indices
        #are returned. first idea is to sort this but it would be n log n
        #how about unsorted?
        # we have a target number
        # x[i] + x[j] = target
        # each number has a 'complement'
        # which is target - n[i] = complement
        # we can build a hashmap, and check if the complement is in 
        #the hashmap
        #should we build a complement array?
        complement_map = {}
        for index, number in enumerate(nums):
            complement = target - number
            if complement in complement_map:
                return [complement_map[complement], index]
            complement_map[number] = index

