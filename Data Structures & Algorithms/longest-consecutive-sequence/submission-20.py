class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #easiest solution that comes to mind is to convert the array
        #into a set, then sort the array
            nums_set = set(nums)
            if len(nums_set) == 0:
                return 0
            if len(nums_set) == 1:
                return 1

            else:
                sorted_set = sorted(nums_set)
                current = 1
                best = 1
                for i in range (len(sorted_set) -1):
                    if sorted_set[i] + 1 == sorted_set[i+1]:
                        current+=1
                        best = max(best, current)
                    else:
                        current = 1
                return max(current, best)
            


        

        