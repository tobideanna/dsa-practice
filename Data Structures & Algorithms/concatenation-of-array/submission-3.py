class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans2 = nums.copy()
        for number in nums:
            ans2.append(number)
        return ans2
        