class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #the other way is to create a map for each,
        #use the letter as the keys, and count of letters
        #as values
        if len(s) != len(t):
            return False
        s_map = defaultdict(int)
        t_map = defaultdict(int)
        for i in range(len(s)):
            #increase the count of said letter by 1
            s_map[s[i]] += 1
            t_map[t[i]] += 1
        return t_map == s_map

        