class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #if not, we can use a set, and add each number to set
        #if number in set, then return true
        checked = set()
        for num in nums:
            if num in checked:
                return True
            else:
                checked.add(num)
        return False