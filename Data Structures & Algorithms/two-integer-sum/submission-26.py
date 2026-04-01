class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #let's use a hash map to store each number
        #then check if complement is in hashmap
        #if complement in hashmap, then return the numbers
        #key is the index
        comp_set = defaultdict(int)

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in comp_set:
                return [comp_set[complement], i]
            
            else:
                comp_set[nums[i]] = i
        return None
            
            