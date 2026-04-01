class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #for anagrams, we want to add each character to a
        #hashmap, and if the count of characters is the same,
        #then they are anagrams
        #or we sort them and compare them?
        countS = defaultdict(int)
        countT = defaultdict(int)
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            countS[s[i]] += 1
            countT[t[i]] += 1
        
        return countS == countT


        