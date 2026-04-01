
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """ check if is anagram. both strings need to be same length
        if they are same length, make a hashmap with their numbers, and
        do key is each character, and value is the number of ocurrences

        """
        countS, countT = {}, {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT  


        