class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            countS, countT = {}, {}
            #create hashmap, and then we need to iterate over each character
            for i in range(len(s)):
            #for each iteration, we need to:
            #1. look at s[i] and t[i]. make countS[s[i]] set to the number
                countS[s[i]] = countS.get(s[i], 0) + 1
                countT[t[i]] = countT.get(t[i], 0) + 1
        return countS == countT
