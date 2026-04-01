class Solution:
    def findMin(self, nums: List[int]) -> int:
        #we are given a sorted array that has been rotated and we will try
        #to find the minimum
        #example: [4,5,0,1,2,3]
        #example: [3,4,5,6,1,2]
        result = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break
            
            midpoint = (l + r) // 2
            result = min(result, nums[midpoint])
            if nums[midpoint] >= nums[l]:
                l = midpoint + 1
            else:
                r = midpoint - 1
        return result

            
                