class Solution:
    def isPalindrome(self, s: str) -> bool:
        #we need to check if string is palindrome. we can do this with
        #2 pointers. transform everything to .lower() and skip every other
        #maybe use = .isalphanum()?
        new = ''
        for char in s:
            if char.isalnum():
                new += char.lower()
        return new == new[::-1]
                
        