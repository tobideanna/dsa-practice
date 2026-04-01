class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #basically, find duplicate in the array, but where
        #the value of i-j <= k, so a window of k, so sliding window
        #initialize a set first to store the window
        window = set()
        L = 0 #initialize left pointer

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False