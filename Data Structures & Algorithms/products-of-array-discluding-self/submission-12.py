class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #we can solve this using prefix and postfix
        pre = [0] * len(nums)
        post = [0] * len(nums)
        pretotal = posttotal = 1
        res = [0] * len(nums)
        for i in range(len(nums)):
            pretotal *= nums[i]
            pre[i] = pretotal
        for i in range(len(nums) - 1, -1, -1):
            posttotal *= nums[i]
            post[i] = posttotal
        
        res[0] = (post[1])
        res[-1] = (pre[-2])
        
        for i in range(1, len(nums)-1):
            res[i] = (pre[i-1] * post [i+1])
        return res