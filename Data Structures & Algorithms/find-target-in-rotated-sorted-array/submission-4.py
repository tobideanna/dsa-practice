class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #we need to find minimum in the rotated array and ret the i
        #examples: [3,4,5,6,1,2] target 1
        #[4,5,6,0,1,2,3], target = 4
        #examples: [1,2,3,4,5,6,7] target 2
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            
            #left sorted
            elif nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]: #target is here
                    r = mid - 1
                else:
                    l = mid + 1
            
            #right sorted
            elif nums[mid] <= nums[r]:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
        
        




