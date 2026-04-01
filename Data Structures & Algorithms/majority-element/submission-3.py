class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #find majority element
        #first idea is to iterate through the array. design a hashmap
        # that maps the value to the number of occurences, then return the key with
        #the highest value
        counts = defaultdict(int)
        for i in range(len(nums)):
            counts[nums[i]] += 1
        return max(counts, key=counts.get)