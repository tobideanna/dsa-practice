class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = defaultdict(int)
        for i, num in enumerate(nums):
            diff = target - nums[i]
            if diff in res:
                return [res[diff], i]
            res[num] = i
        