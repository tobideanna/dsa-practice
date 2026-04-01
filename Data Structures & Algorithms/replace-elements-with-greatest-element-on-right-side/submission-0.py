class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ''' so let's say we have arr = [2,4,5,3,1,2]
        we need to first set a variable to -1, the last of the array
        after that, we need to compare that to the last value of the array
        then you compute the max of that number and the

        '''

        #initialize a new array
        n = len(arr)
        ans = [0] * n
        right_max = -1
        for i in range(n-1, -1, -1):
            ans[i] = right_max
            right_max = max(arr[i], right_max)
        return ans

        
