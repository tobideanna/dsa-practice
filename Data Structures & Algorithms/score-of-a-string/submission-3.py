class Solution:
    def scoreOfString(self, s: str) -> int:
        #calculate scores of words: e.g:
        #hello. so we need to take the pairs he, el, ll, lo first. then 
        #calculate the ascii value for each, and then substract the first from second
        score = 0
        for i in range(len(s) -1 ):
            score += abs(ord(s[i]) - ord(s[i+1]))
        return score
        
