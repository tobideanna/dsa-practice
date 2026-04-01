class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, r1 = 0, len(word1) - 1
        l2, r2 = 0, len(word2) - 1
        res = ""
        if len(word2) > len(word1):
            while l2 <= r2:
                while l1 <= r1:
                    res += (word1[l1])
                    res += (word2[l2])
                    l1 += 1
                    l2 += 1
                res += (word2[l2])
                l2 += 1
            return res
        
        elif len(word1) > len(word2):
            while l1 <= r1:
                while l2 <= r2:
                    res += (word1[l1])
                    res += (word2[l2])
                    l1 += 1
                    l2 += 1
                res += (word1[l1])
                l1 += 1
            return res

        else:
            while l1 <= r1:
                    res += word1[l1]
                    res += word2[l2]
                    l1 += 1
                    l2 += 1
            return res

        
                


        