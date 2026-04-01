class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        '''
        s is a string. we know that it hsa spaces and letters
        i would think i would iterate backwards from the string
        initialize a counter variable
        if character

        while character is a letter
        if the character is a letter, counter+=1
        return counter

        '''
        i = (len(s) - 1)
        counter = 0
        while i>= 0 and s[i] == ' ':
            i-=1

        while i>= 0 and s[i] != ' ':
            counter += 1
            i-=1
        return counter

        
        'hello'
        '12345'
            
