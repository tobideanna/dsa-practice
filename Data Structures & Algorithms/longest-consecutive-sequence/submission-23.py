class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #let's try the optimal solution. still using a set
        nums_set = set(nums)
        longest = 0
        # we need to start at start of sequences, so check if the number
        # doesn't have a -1, which is what it would be
        for number in nums_set:
            if number - 1 not in nums_set:
                length = 0
                while number + length in nums_set:
                    length += 1
                longest = max(length, longest)
        return longest
