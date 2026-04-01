class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #we identify the start of a sequence by finding if nums-1
        #not in array
        if not nums:
            return 0
        curr_seq = 1
        max_sequence = 1
        for num in nums:
            if num-1 not in nums:
                curr_seq = 1
                while num+1 in nums:
                    curr_seq += 1
                    max_sequence = max(max_sequence, curr_seq)
                    num += 1
        return max_sequence

                


        