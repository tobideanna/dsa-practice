class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_nums = nums.copy()
        for num in new_nums:
            nums.append(num)
        return nums