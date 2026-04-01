class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ''' check if is subsequence. so basically grab each character, and check if
            the char is in t. if all of them are true, return true

        '''
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+= 1
                j+=1
            else:    
                j+=1
        return i == len(s)

    

