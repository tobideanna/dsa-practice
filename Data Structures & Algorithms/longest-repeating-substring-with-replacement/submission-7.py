class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #ok, we are given a string e.g. #"ABABBA" and we need to figure out the
        #longest substring, with max k replacements, so that we get the largest
        #substring
        #we can use a sliding window
        # "ABABBA"
        l = 0
        count = defaultdict(int) #count number of ocurrences
        res = 0
        #we iterate through the whole array
        for r in range(len(s)):
            count[s[r]] += 1

            while r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
            
        return res





        

            


        

        