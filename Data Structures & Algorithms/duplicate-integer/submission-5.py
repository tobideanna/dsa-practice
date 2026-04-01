class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
           #check if contains duplicate:
           # for each item in the array, compare that with every other item in the array
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i] == nums[j]:
                        return True
            return False
            

                
