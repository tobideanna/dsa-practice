class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
           #the other solution is to use a hash_map, where:
           #initialize empty dict
            my_dict = {}
            #we should add in the dictionary with a key:value pair
            #if item not in dict, then add it with value 1
            #if item already in dict, return True
            for i, element in enumerate(nums):
                if element in my_dict:
                    return True
                else:
                    my_dict[element] = 1
            return False
            

                
