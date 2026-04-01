class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #for anagrams, we want to add each character to a
        #hashmap, and if the count of characters is the same,
        #then they are anagrams
        #or we sort them and compare them?
        return sorted(s) == sorted(t)
        