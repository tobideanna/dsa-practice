class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #another solution is a hashmap. So, think of target as a complement number,
        #so the difference = target - nums[i].
        """ we need to find that number in the hashmap. we also need to return indices,
        not values. so we probably need to use enumerate to keep track of both
        steps:
        1. iterate through each element of the array
        2. calculate diff for each element of the array
        3. if diff is in hashmap, return i,j indices as an array.
        4. if not, add elements to hashmap. """
        checked_map = {}
        for index, value in enumerate(nums):
            difference = target - value
            if difference in checked_map:
                return [checked_map[difference], index]
            checked_map[value] = index
