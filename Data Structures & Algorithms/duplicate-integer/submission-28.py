class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #if not, we can use a set, and add each number to set
        #if number in set, then return true
        return len(nums) != len(set(nums))