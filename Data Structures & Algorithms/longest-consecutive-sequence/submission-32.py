class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #we identify the start of a sequence by finding if nums-1
        #not in array
        numSet = set(nums)
        if not nums:
            return 0
        curr_seq = 1
        max_sequence = 1
        for num in numSet:
            if num-1 not in numSet:
                curr_seq = 1
                while num+1 in numSet:
                    curr_seq += 1
                    num += 1
                max_sequence = max(max_sequence, curr_seq)
        return max_sequence

                


        