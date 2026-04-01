class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #we need to find longest substring without repeating chars
        #we can do this by using sliding window, and using a set as
        #the window. then, we add characters to the window
        #pseudocode
        window = set()
        longest = 0
        L = 0

        for R in range(len(s)):
            if s[R] not in window:
                window.add(s[R])
                longest = max(longest, R - L + 1)
            else:
                while s[R] in window:
                    window.remove(s[L])
                    L += 1
                window.add(s[R])
                longest = max(longest, R - L + 1)
        return longest

                
               
            


