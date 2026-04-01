class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping = defaultdict(list)
        for string in strs:
            signature = [0] * 26
            for char in string:
                key = ord(char) - ord('a')
                signature[key] += 1
            grouping[tuple(signature)].append(string)
        return list(grouping.values())
        

        


        