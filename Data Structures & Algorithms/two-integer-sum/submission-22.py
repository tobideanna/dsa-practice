class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #another solution is a hashmap. So, think of target as a complement number,
        #so the complement = target - nums[i].
        """we need to find if complement is in hashmap
        for that, we build a hashmap, in the hashmap, we look if the complement is there
        if the complement is not there, then put it in the hashmap.
        if the copmlement is in hashmap, return index and the number of current iteration

        e.g. [1,2,4]:
        comp1 = 5
        comp2 = 4
        comp3 = 2
        """
        hash_check = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement not in hash_check:
                hash_check[value] = index
            else:
                return [hash_check[complement], index]
                print (hash_check)
            
