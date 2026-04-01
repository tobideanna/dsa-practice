'''
we need to, in each point of the array, replace it
with all the multiplications of the numbers except self
we can do this with prefix and postfix multiplications

first, we calculate prefix and postfix for each number in the array
'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        postfix = [0] * n
        res = [0] * n
        
        prefix[0] = postfix[n-1] = 1
        
        '''iterate the number of times for each item in array
        if array has 5 items in it, iterate 5 times'''
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
        '''now let's do postfix'''
        for i in range(n-2, -1, -1):
            postfix[i] = nums[i+1] * postfix[i+1]
        for i in range(n):
            res[i] = prefix[i] * postfix[i]
        return res

        
    