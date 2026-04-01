class Solution:
    def isPalindrome(self, s: str) -> bool:
        #one solution that comes to mind is to strip all " " from the word
        #idk if that takes a long time
        new_s = ""
        for char in s:
            if char.isalnum():
                new_s += char.lower()
            else:
                continue
            
        
        L, R = 0, len(new_s) - 1
        
        while L < R:
            if new_s[L] == new_s[R]:
                L += 1
                R -= 1
            else:
                return False
        return True
