class Solution:
    def isPalindrome(self, s: str) -> bool:
        #we need to check if string is palindrome. we can do this with
        #2 pointers. transform everything to .lower() and skip every other
        #maybe use = .isalphanum()?
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1, r- 1
        return True
                
        