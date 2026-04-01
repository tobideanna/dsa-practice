class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we want to know if two strings are anagrams
        # this means the count of each character is the same
        #this means that we can use a hashmap, put each letter
        # as the key, and count as the value. if they are the same,
        # then they are anagrams
        # or maybe cleaner with a set?
        return sorted(s) == sorted(t)